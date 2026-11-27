"""Nối model — chỗ DUY NHẤT trong bản chạy thử gọi model AI.

Hợp đồng (giữ nguyên để khung đo được token):
    call_model(system: str, user: str) -> dict với 4 khoá
        "text":       str   chữ model trả về
        "model":      str   tên model đã gọi (để tra giá ở bảng giá model)
        "tokens_in":  int   số token vào, lấy từ trường usage trong phản hồi API — KHÔNG ước lượng
        "tokens_out": int   số token ra, gồm cả token suy luận / suy nghĩ nếu API tính riêng
    @model_call (từ tracing.py) tự ghi mỗi lần gọi vào trace; agent.py gọi call_model bao nhiêu lần
    cũng được, khung tự cộng token.
    Lỗi gọi model (hết lượt, sai key, mất mạng): cứ để exception bay ra — khung ghi lỗi vào cột error.

Chế độ giả (mặc định khi .env chưa có MODEL_PROVIDER, hoặc MODEL_PROVIDER=fake):
    trả một câu giả cố định, model "fake", token 0 — để luồng chạy hết từ trước CP2 (guide bước 3.2).
    Lượt `run.py eval` / `run.py simulate` chạy bằng model giả KHÔNG được tính.

Đã có kết nối Gemini, OpenAI, Anthropic bằng thư viện chuẩn. Điền .env theo README.md.
Không dán API key vào file này. Kết nối thật cần kiểm tra bằng key của nhóm.
"""
import json
import os
import urllib.error
import urllib.parse
import urllib.request

from tracing import model_call

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_env(path=os.path.join(ROOT, ".env")):
    """Đọc file .env (KEY=VALUE mỗi dòng) vào biến môi trường, không ghi đè biến đã có. Khung — không cần sửa."""
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8-sig") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


load_env()
MODEL_PROVIDER = (os.environ.get("MODEL_PROVIDER") or "fake").strip().lower()
MODEL_NAME = (os.environ.get("MODEL_NAME") or "").strip()
API_KEY = (os.environ.get("API_KEY") or "").strip()


@model_call
def call_model(system: str, user: str) -> dict:
    if MODEL_PROVIDER == "fake":
        last = (user.strip().splitlines() or [""])[-1]
        return {"text": "[câu trả lời giả — chưa nối model] " + last[:60], "model": "fake", "tokens_in": 0, "tokens_out": 0}

    providers = {"gemini": call_gemini, "openai": call_openai, "anthropic": call_anthropic}
    if MODEL_PROVIDER not in providers:
        raise ValueError("MODEL_PROVIDER phải là fake, gemini, openai hoặc anthropic.")
    if not MODEL_NAME or not API_KEY:
        raise ValueError("Thiếu MODEL_NAME hoặc API_KEY. Điền .env theo README.md.")
    result = providers[MODEL_PROVIDER](system, user)
    if not isinstance(result["text"], str) or not result["text"].strip():
        raise RuntimeError("API không trả văn bản; kiểm tra bộ lọc nội dung hoặc giới hạn output.")
    return result


def post_json(url, headers, body):
    """Gọi API JSON với timeout; không đưa key hay nội dung phản hồi lỗi vào trace."""
    request = urllib.request.Request(
        url, data=json.dumps(body).encode("utf-8"), method="POST",
        headers={"Content-Type": "application/json", **headers})
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        hints = {400: "Kiểm tra tên model và định dạng yêu cầu.",
                 401: "Kiểm tra API key.", 403: "Kiểm tra quyền truy cập model.",
                 404: "Kiểm tra tên model.", 429: "Hết quota hoặc quá giới hạn lượt gọi."}
        error.close()
        raise RuntimeError("API HTTP %d. %s" % (
            error.code, hints.get(error.code, "Nhà cung cấp gặp lỗi; thử lại sau."))) from None
    except (urllib.error.URLError, TimeoutError):
        raise RuntimeError("Không kết nối được API hoặc quá thời gian chờ 60 giây.") from None
    except (ValueError, UnicodeError):
        raise RuntimeError("API trả phản hồi JSON không hợp lệ.") from None


def token_count(usage, key, optional=False):
    """Chỉ nhận số đo token từ API; trường bắt buộc bị thiếu phải báo lỗi."""
    value = usage.get(key, 0) if optional else usage[key]
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError("API trả số token không hợp lệ ở trường %s." % key)
    return value


def call_gemini(system, user):
    body = {"contents": [{"role": "user", "parts": [{"text": user}]}]}
    if system:
        body["systemInstruction"] = {"parts": [{"text": system}]}
    model = urllib.parse.quote(MODEL_NAME, safe="")
    data = post_json("https://generativelanguage.googleapis.com/v1beta/models/%s:generateContent" % model,
                     {"x-goog-api-key": API_KEY}, body)
    candidates = data.get("candidates") or []
    if not candidates:
        raise RuntimeError("Gemini không trả candidate; yêu cầu có thể bị bộ lọc nội dung chặn.")
    parts = candidates[0].get("content", {}).get("parts", [])
    text = "".join(p.get("text", "") for p in parts if not p.get("thought"))
    usage = data["usageMetadata"]
    return {"text": text, "model": data.get("modelVersion") or MODEL_NAME,
            "tokens_in": token_count(usage, "promptTokenCount"),
            "tokens_out": token_count(usage, "candidatesTokenCount")
                          + token_count(usage, "thoughtsTokenCount", optional=True)}


def call_openai(system, user):
    messages = ([{"role": "system", "content": system}] if system else [])
    messages.append({"role": "user", "content": user})
    data = post_json("https://api.openai.com/v1/chat/completions",
                     {"Authorization": "Bearer " + API_KEY},
                     {"model": MODEL_NAME, "messages": messages, "store": False})
    usage = data["usage"]
    # completion_tokens đã gồm reasoning_tokens; không cộng lần hai.
    return {"text": data["choices"][0]["message"]["content"],
            "model": data.get("model") or MODEL_NAME,
            "tokens_in": token_count(usage, "prompt_tokens"),
            "tokens_out": token_count(usage, "completion_tokens")}


def call_anthropic(system, user):
    data = post_json("https://api.anthropic.com/v1/messages",
                     {"x-api-key": API_KEY, "anthropic-version": "2023-06-01"},
                     {"model": MODEL_NAME, "max_tokens": 2048, "system": system,
                      "messages": [{"role": "user", "content": user}]})
    usage = data["usage"]
    return {"text": "".join(b.get("text", "") for b in data.get("content", [])
                            if b.get("type") == "text"),
            "model": data.get("model") or MODEL_NAME,
            "tokens_in": token_count(usage, "input_tokens")
                         + token_count(usage, "cache_creation_input_tokens", optional=True)
                         + token_count(usage, "cache_read_input_tokens", optional=True),
            "tokens_out": token_count(usage, "output_tokens")}
