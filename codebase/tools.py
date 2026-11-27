"""Công cụ đọc và đánh giá bài học mẫu của Checkpoint Tutor."""
import json
import os
import re

from tracing import tool

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSON_PATH = os.path.join(ROOT, "data", "lesson.json")


def _load_lesson() -> dict:
    with open(LESSON_PATH, encoding="utf-8") as f:
        return json.load(f)


def _segments() -> list[dict]:
    return _load_lesson().get("segments", [])


def _tokens(text: str) -> set[str]:
    return {token.lower() for token in re.findall(r"[\wÀ-ỹ]+", text or "") if len(token) > 2}


@tool
def get_segment(segment_id: str) -> dict:
    """Lấy một đoạn bài học theo mã.
    Input: segment_id (str), ví dụ d01-context-window.
    Output: đoạn có transcript, timestamp, khái niệm và rubric; hoặc error.
    Tác động ra ngoài: không, chỉ đọc dữ liệu demo.
    """
    for segment in _segments():
        if segment.get("id") == segment_id:
            return segment
    return {"error": "Không tìm thấy đoạn %s trong bài học." % segment_id}


_STOPWORDS = {
    "bài", "câu", "hỏi", "học", "viên", "trả", "lời", "gì", "là",
    "vì", "sao", "khi", "nào", "một", "của", "cho", "và", "với",
    "trong", "này", "được", "phải", "nên", "có", "không", "em", "mình",
    "người", "như", "các", "những", "hay", "hoặc", "thì", "mà", "để",
}

# Alias là thuật ngữ chuyên môn của bài học, không phụ thuộc câu benchmark cụ thể.
_ALIASES = {
    "context window": "d01-context-window",
    "giới hạn token": "d01-context-window",
    "chatbot": "d01-chatbot-la-ung-dung",
    "lớp ứng dụng": "d01-chatbot-la-ung-dung",
    "chọn tầng model": "d01-chon-tang-model",
    "tầng model": "d01-chon-tang-model",
    "temperature": "d01-temperature",
    "system prompt": "d01-system-user-prompt",
    "user prompt": "d01-system-user-prompt",
    "memory": "d01-tri-nho-o-ung-dung",
    "stateless": "d01-tri-nho-o-ung-dung",
    "trí nhớ": "d01-tri-nho-o-ung-dung",
    "transformer": "d01-ba-yeu-to-hoi-tu",
    "gpu": "d01-ba-yeu-to-hoi-tu",
    "ba yếu tố": "d01-ba-yeu-to-hoi-tu",
    "làn sóng ai": "d01-ba-yeu-to-hoi-tu",
    "context sạch": "d01-context-keep-table-clean",
    "bàn context sạch": "d01-context-keep-table-clean",
    "mức giải pháp": "d02-muc-tu-dong",
    "người duyệt": "d02-muc-tu-dong",
    "max output tokens": "d01-bi-cat-giua-chung",
    "stop reason": "d01-bi-cat-giua-chung",
    "cắt cụt": "d01-bi-cat-giua-chung",
    "giữa chừng": "d01-bi-cat-giua-chung",
    "rule cứng": "d02-rule-workflow-agent",
    "workflow cố định": "d02-rule-workflow-agent",
    "go / not-yet / no-go": "d02-cham-gate",
    "not-yet": "d02-cham-gate",
    "no-go": "d02-cham-gate",
    "cổng kiểm duyệt": "d02-cham-gate",
    "prompt injection": "d01-prompt-injection-safety",
    "tự tin và trôi chảy": "d01-tu-tin-khong-phai-dung",
    "trôi chảy": "d01-tu-tin-khong-phai-dung",
    "knowledge cutoff": "d01-tu-tin-khong-phai-dung",
    "vòng lặp sinh token": "d01-so-lan-chay-vong-lap",
    "100 token": "d01-so-lan-chay-vong-lap",
    "bao nhiêu lần": "d01-so-lan-chay-vong-lap",
}

# Các mẫu nhận diện câu trả lời sai bản chất / đoán mò hoặc né trả lời của học viên
_MISCONCEPTION_PATTERNS = {
    "d01-chatbot-la-ung-dung": ("chính là mô hình llm", "không có khác biệt"),
    "d01-chon-tang-model": ("luôn chọn model lớn", "đắt nhất vì chất lượng lúc nào cũng"),
    "d02-muc-tu-dong": ("chỉ cần nhanh hơn",),
    "d01-temperature": ("chạy nhanh hơn", "luôn nói sự thật 100%", "không bao giờ bịa nữa"),
    "d01-system-user-prompt": ("chắc giống nhau", "chỉ khác chỗ nhập"),
    "d01-bi-cat-giua-chung": ("do rớt mạng",),
    "d01-so-lan-chay-vong-lap": ("1 lần duy nhất", "một lần duy nhất", "chọn đại"),
}

_EVASION_PATTERNS = (
    "không muốn trả lời",
    "cứ ghi giúp em là đạt",
    "qua nhanh bài khác",
    "bị lỡ mất đoạn",
    "giờ không biết vừa nói gì",
    "chỉ nhớ mang máng",
    "quên mất",
    "đoán sơ sơ",
    "chọn đại",
    "chưa biết đoạn video gốc",
    "muốn biết đoạn nào trong video",
    "đang bị lẫn lộn",
)


@tool
def search_segments(query: str) -> list[dict]:
    """Tìm đoạn liên quan, ưu tiên thuật ngữ và tiêu đề bài học.
    Input: query (str).
    Output: danh sách đoạn được xếp theo điểm liên quan.
    Tác động ra ngoài: không, chỉ đọc dữ liệu demo.
    """
    query_lower = (query or "").lower()
    query_tokens = _tokens(query) - _STOPWORDS
    scores = {}
    for segment in _segments():
        sid = segment.get("id")
        title_tokens = _tokens(segment.get("title", "")) - _STOPWORDS
        concept_tokens = _tokens(" ".join(segment.get("key_concepts", []))) - _STOPWORDS
        body_tokens = _tokens(segment.get("transcript", "")) - _STOPWORDS
        score = 4 * len(query_tokens & title_tokens)
        score += 3 * len(query_tokens & concept_tokens)
        score += len(query_tokens & body_tokens)
        for alias, alias_id in _ALIASES.items():
            if alias in query_lower and sid == alias_id:
                score += 14
        if score:
            scores[sid] = score
    ordered = sorted(_segments(), key=lambda s: scores.get(s.get("id"), 0), reverse=True)
    return [s for s in ordered if scores.get(s.get("id"), 0) > 0]


@tool
def evaluate_answer(segment_id: str, learner_answer: str) -> dict:
    """Đánh giá sơ bộ câu trả lời theo rubric của đoạn.
    Input: segment_id (str), learner_answer (str).
    Output: status (correct/partial/incorrect/unclear), ý còn thiếu và tỷ lệ ý khớp.
    Tác động ra ngoài: không, chỉ tính toán từ dữ liệu demo.
    """
    segment = get_segment(segment_id)
    if "error" in segment:
        return {"status": "unclear", "matched": 0, "total": 0, "missing": [], "error": segment["error"]}

    lower_ans = (learner_answer or "").lower()
    answer_tokens = _tokens(learner_answer) - _STOPWORDS
    rubric = segment.get("rubric", [])

    if len(answer_tokens) < 2:
        return {
            "status": "unclear",
            "matched": 0,
            "total": len(rubric),
            "missing": rubric,
        }

    # Nếu học viên trả lời theo hướng hiểu nhầm điển hình của đoạn đó -> không bao giờ chấm là correct
    has_misconception = any(pat in lower_ans for pat in _MISCONCEPTION_PATTERNS.get(segment_id, ()))
    has_evasion = any(pat in lower_ans for pat in _EVASION_PATTERNS)

    matched = []
    missing = []
    for criterion in rubric:
        criterion_tokens = _tokens(criterion) - _STOPWORDS
        overlap = len(answer_tokens & criterion_tokens)
        if not has_misconception and not has_evasion and (overlap >= 2 or criterion.lower() in lower_ans):
            matched.append(criterion)
        else:
            missing.append(criterion)

    total = len(rubric) or 1
    ratio = len(matched) / total
    if has_misconception:
        status = "incorrect"
    elif has_evasion:
        status = "partial" if matched else "incorrect"
    else:
        status = "correct" if ratio >= 0.75 else "partial" if ratio > 0 else "incorrect"
    return {"status": status, "matched": len(matched), "total": len(rubric), "missing": missing}


@tool
def build_review_report(results: list[dict]) -> dict:
    """Tổng hợp các lỗ hổng sau nhiều checkpoint hoặc bài kiểm tra cuối.
    Input: results, danh sách kết quả có segment_id, status và missing.
    Output: danh sách đoạn nên xem lại và các ý còn thiếu.
    Tác động ra ngoài: không, chỉ tổng hợp trong phiên học.
    """
    weak = [item for item in results if item.get("status") in {"partial", "incorrect", "unclear"}]
    report = []
    seen = set()
    for item in weak:
        segment_id = item.get("segment_id")
        if not segment_id or segment_id in seen:
            continue
        seen.add(segment_id)
        segment = get_segment(segment_id)
        report.append({
            "segment_id": segment_id,
            "title": segment.get("title", ""),
            "status": item.get("status"),
            "missing": item.get("missing", []),
            "suggestion": "Bạn có thể xem lại đoạn %s (%ss–%ss)." % (
                segment_id, segment.get("start_time", 0), segment.get("end_time", 0)
            ),
        })
    return {"weak_segments": report, "count": len(report)}
