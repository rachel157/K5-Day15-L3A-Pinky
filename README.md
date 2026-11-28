# Pinky — Checkpoint Tutor

> Repo nộp bài Mini Hackathon AI20K (Lớp **L3A** · **Track A — EdTech**). Giờ, mốc, luật, rubric: xem `README.md`, `02-guide.md`, `03-rubric.md` trong bộ đề BTC phát.

**Thành viên, lớp, track:** xem [TEAMS.md](TEAMS.md). **Điền TEAMS.md đúng format**: khi chấm và đánh giá, BTC quét file này để ghép điểm cho từng người.

*Lát cắt = phần nhỏ nhất làm xong được trong hackathon: một người dùng · một việc · một quyết định AI · một kết quả.*

---

## Nhóm làm gì, khung làm gì

| Nhóm quyết định và viết | Khung làm sẵn (không cần sửa) |
|---|---|
| Người dùng, pain, bằng chứng, impact (`evidence/`, `spec.md` §1–§2) | — |
| Hình dạng giải pháp, công cụ, prompt, luồng (`spec.md` §4, `codebase/agent.py`, `tools.py`, `ai.py`) | Ghi mọi lần gọi model / công cụ vào trace, cộng token (`codebase/tracing.py`) |
| Bộ câu thử, metric, chuẩn "đạt" (`eval/benchmark.csv`, `eval/metric_spec.yaml`, `spec.md` §7) | Kiểm đủ cột, đủ câu `kho` / `tu_choi`, đủ ≥1/3 câu từ người dùng / data thật (`run.py check`) |
| Chấm cột `pass` theo metric spec | Chạy cả bộ một lệnh, có run ID, model, token từng câu (`run.py eval`) · tính % đạt (`run.py score`) |
| Persona, số người dùng thật, giá model (`cost/personas.yaml`) | Sinh ~50 phiên, chạy thật qua bản chạy thử, tính chi phí / phiên, / task thành công, / tháng 3 kịch bản (`run.py simulate`) |

*Ví dụ track A (ví dụ cỡ, không phải lời giải):* nhóm viết công cụ `search_lesson` tra bài pre-class đã đánh mã đoạn, luồng "tra đoạn → model trả lời kèm mã đoạn, không có thì nói không có", metric "mọi khẳng định có mã đoạn đúng", persona "ôn dồn trước kiểm tra". Khung chạy 25 câu thử ra `run-1.csv`, nhóm chấm `pass`, `score` in % đạt; `simulate` chạy 50 phiên ra chi phí / task thành công cho hai model.

## Chạy trong 3 phút

Bộ khung cần **Python 3.10 trở lên** (Python 3.9 có sẵn trên macOS vẫn chạy được, chỉ in một dòng nhắc). **Không cần `pip install`.**

**Bước 1 — Mở cửa sổ lệnh ngay trong thư mục repo**

| Windows (PowerShell) | macOS |
|---|---|
| Mở thư mục repo bằng File Explorer → bấm vào thanh địa chỉ → gõ `powershell` → Enter | Mở **Terminal** (Cmd + Space, gõ "Terminal") → gõ `cd ` (có dấu cách) → kéo thả thư mục repo vào → Enter |

Gõ `dir` (Windows) hoặc `ls` (macOS / Linux): thấy `run.py` và `README.md` là đang đứng đúng chỗ.

**Bước 2 — Kiểm Python và chạy thử**

| Việc | Windows (PowerShell) | macOS / Linux |
|---|---|---|
| Kiểm Python | `python --version` (không được thì `py --version`) | `python3 --version` |
| Chạy bản chạy thử (chế độ giả, chưa gọi model) | `python run.py` | `python3 run.py` |
| Kiểm bộ câu thử | `python run.py check` | `python3 run.py check` |
| Tạo file `.env` để nối model | `copy .env.example .env` | `cp .env.example .env` |

- Windows: gõ `python` mà mở Microsoft Store hoặc báo không có lệnh → dùng `py`. Chưa có Python: cài từ python.org, **tick "Add python.exe to PATH"**, mở lại PowerShell.
- macOS: báo `command not found: python` là bình thường → dùng `python3`.
- `python run.py` in ra "[câu trả lời giả — chưa nối model] …" là khung chạy đúng. Nối model thật: [docs/connect-model.md](docs/connect-model.md).

Trong README này lệnh viết là `python …`; máy nhóm cần `python3` hay `py` thì gõ thay.

## Lệnh

| Lệnh | Làm gì |
|---|---|
| `python run.py` | Chạy bản chạy thử dòng lệnh (gõ đầu vào, nhận kết quả, kèm số lần gọi model / token) |
| `python demo/demo_server.py` | **Chạy giao diện Web Demo (http://127.0.0.1:8765):** Trình phát video chuẩn YouTube có mốc Checkpoint nổi trên video (Trắc nghiệm & Tự luận chấm bằng LLM thật), hàng đợi câu hỏi khi tua qua nhiều đoạn, danh sách Checkpoint thu gọn/mở rộng và khung Chat Trợ giảng AI bám phụ đề video |
| `python run.py check` | Kiểm `eval/benchmark.csv` (6 cột, số câu, `kho` / `tu_choi`, mã `source`, ô trống, dòng mẫu) `eval/metric_spec.yaml` (≥3 metric điền đủ) và `TEAMS.md` (đúng format để BTC quét). Chỉ cảnh báo, không sửa file |
| `python run.py eval --try` | **Thử nối model:** chạy 3 câu đầu (`--try 5` = 5 câu) → `eval/run-try.csv`. Thấy "Nối model được" là xong. Không tính là một lượt |
| `python run.py eval` | Chạy cả bộ qua `codebase/agent.py` → `eval/run-1.csv` (lần sau `run-2.csv`…) + `traces/run-1.jsonl`. Mỗi dòng có run ID, model, số lần gọi model / công cụ, token. Model còn giả → chỉ ghi `run-mock.csv`; mọi câu lỗi → `run-error.csv`; Ctrl+C → `run-stopped.csv` — đều **không** được đánh số |
| `python run.py eval --fake` | Thử riêng bộ chạy, không gọi agent → `eval/run-fake.csv` |
| `python run.py score eval/run-1.csv` | Sau khi điền cột `pass` (1 / 0): in % đạt tổng và theo `type`. Còn ô trống → "CHƯA CHẤM XONG", không in % |
| `python run.py simulate --try` | Thử mô phỏng chi phí 10 phiên (làm trước CP3) → `cost/simulate-try.csv` |
| `python run.py simulate` | Mô phỏng chi phí khi dùng thật theo `cost/personas.yaml` (≥50 phiên) → `cost/simulate-N.csv` + `cost/simulate-N-summary.md` |
| `python run.py simulate --rate-from eval/run-2.csv` | Như trên, lấy tỉ lệ đạt từ đúng lượt chỉ định. Không ghi thì khung lấy lượt `run-N` mới nhất đã chấm, cùng model, và ghi rõ đã lấy lượt nào trong bản tóm tắt |

Gói miễn phí báo hết lượt: thêm `--wait 4` sau `eval` hoặc `simulate` (nghỉ 4 giây giữa hai lượt gọi). Sửa CSV bằng Excel: *File → Save As → CSV UTF-8*; Google Sheets: *Tệp → Tải xuống → CSV*.

**Lượt có lỗi kỹ thuật** (cột `error` có chữ): không sửa tay file đó, chạy lại thành lượt mới và ghi vào bảng các lượt ở `eval/README.md`. Không xoá file lượt nào.

Nhóm dùng stack khác (Node, Streamlit, notebook…): sửa hàm `run_app()` trong `run.py` để `python run.py` vẫn chạy được bản chạy thử, và giữ `answer()` trong `codebase/agent.py` để `eval`, `simulate` chạy được.

## Bản chạy thử — viết ở đâu

| File | Viết gì | Bước guide |
|---|---|---|
| `codebase/agent.py` | `answer(text)` — luồng chính, đúng hình dạng ở `spec.md` §4. Khung có sẵn một workflow 2 bước *ví dụ* | 3.2 |
| `codebase/tools.py` | Công cụ của bài toán, mỗi công cụ một hàm có `@tool` | 2.2, 3.2 |
| `codebase/ai.py` | `call_model(system, user)` — chỗ duy nhất gọi model. Chưa điền `.env` thì chạy **chế độ giả** | 3.3 |

- **Trước CP2:** để chế độ giả, công cụ trả dữ liệu giả — `python run.py` đi hết luồng là đủ.
- **Trước CP3:** nối model thật theo [docs/connect-model.md](docs/connect-model.md), `eval --try` thấy token > 0 rồi mới `eval`.
- Bộ chạy gửi **nguyên ô `input`** của câu thử vào `answer(text)`. Dữ liệu nền (bài học, thông báo, lịch…) để trong `data/`, đọc qua công cụ.

## Phần nào thật, phần nào giả

| Thành phần | Thật / Giả | Ghi chú |
|---|---|---|
| Lời gọi AI ở quyết định trung tâm | **Thật** (bắt buộc từ CP3) | Model: `gpt-5.4-mini` (`gpt-5.4-mini-2026-03-17` qua OpenAI API, đo đúng `tokens_in`/`tokens_out` từ `usage`; tự lùi về `fake` khi chưa có `.env`) |
| Công cụ tra cứu bài giảng (`codebase/tools.py` + `data/lesson.json`) | **Giả lập có kiểm soát (`synthetic`)** | Đọc **15 đoạn** tóm tắt mẫu Day01 & Day02 biên tập theo danh mục `kc_code` thật, chưa kết nối trực tiếp DB `preclass-online.com` |
| Nhật ký hành vi học tập (`data/preclass`) | **Thật** | Log ẩn danh BTC cấp (dùng đếm bằng chứng qua `evidence/count.py`, không commit file dữ liệu gốc) |

## Dùng AI vào việc gì

2–3 dòng (bắt buộc): nhóm dùng công cụ AI nào để làm gì, người kiểm lại phần nào. Chi tiết: [docs/ai-usage.md](docs/ai-usage.md). Coding agent đọc [AGENTS.md](AGENTS.md).

Nhóm sử dụng coding agent (Codex, Antigravity) để hỗ trợ viết adapter gọi model chuẩn (`codebase/ai.py`), chạy kiểm tra bộ câu thử/mô phỏng chi phí, viết script kiểm tự động 2 metric `code` (`eval/check_code_metrics.py`) và tổng hợp bản nháp báo cáo kỹ thuật. Mọi số liệu bằng chứng đào từ log thật, tiêu chí chấm, cột `pass` và quyết định thiết kế đều do thành viên nhóm trực tiếp đối chiếu, kiểm chứng và duyệt lại.

## File mẫu — điền ở bước nào

| File | Điền ở bước guide | Mốc |
|---|---|---|
| `TEAMS.md` | 1.0 | CP1 · **đúng format**, BTC quét khi chấm |
| `canvas.md` | 1.4 | CP1, cập nhật CP2 |
| `evidence/hypothesis.md` | 1.1 | trước khi tìm bằng chứng |
| `evidence/data-mining.md` · `evidence/interviews/TEMPLATE.md` → `P1.md`… · `evidence/survey/TEMPLATE.md` | 1.2 | bắt đầu sau Zoom, xong CP3 |
| `evidence/summary.md` | 1.2 | CP3 |
| `spec.md` | §0–§2: 1.1–1.3 · §3–§5: 2.1–2.3 · §7: 2.4 · §8: 4.2 · §10: suốt | §7 chốt CP2 · §0–§7 CP3 · đủ CP4 |
| `data/DATA_CARD.md` | 2.4 | bản đầu CP2 |
| `eval/benchmark.csv` · `eval/metric_spec.yaml` | 2.4 | ≥10 câu + metric chốt CP2 · 20–30 câu CP3 |
| `codebase/` | 3.2, 3.3 | khung CP2 · AI thật CP3 |
| `eval/report.md` · `eval/README.md` | 4.1 (README mục 1–4 từ 2.4) | CP4 |
| `cost/personas.yaml` · `cost/cost-estimate.md` | 4.2 | thử 10 phiên CP3 · đủ CP4 |
| `validation/log.md` *(bonus)* | 4.3 | CP4 |
| `slides/outline.md` → `demo-slides.pdf` | 5.1 | CP4 |
| `reflection/TEMPLATE.md` → `reflection/<ten>.md` | 5.3 | 23:59 Thứ Bảy 28/11 |
| `AGENTS.md` · `docs/ai-usage.md` | khi dùng coding agent / AI | suốt |

## Cấu hình và vận hành — phần Vũ

Kết nối Gemini/OpenAI/Anthropic đã có trong `codebase/ai.py`, không cần cài thêm SDK.
Tạo `.env` từ `.env.example` nếu chưa có, rồi điền trên máy:

```dotenv
MODEL_PROVIDER=openai
MODEL_NAME=gpt-5.4-mini
API_KEY=KEY_CUA_NHOM
```

Không commit `.env`. Chạy `python run.py`, nhập một câu và kiểm tra token vào/ra >0.
Ngày 27/11/2026 đã thử input `Reply briefly with OK.`, nhận `OK` từ
`gpt-5.4-mini-2026-03-17`, 45 token vào / 4 token ra, 1 model call và 1 tool call.
Đã chạy `python run.py check` hợp lệ và eval đủ 22 câu bằng AI thật (`gpt-5.4-mini-2026-03-17`), 0 lỗi runtime qua 2 lượt:
- **Lượt 1 (`run-1@20261127-190536`):** đạt **13/22 (59%)** ([eval/run-1.csv](eval/run-1.csv)).
- **Lượt 2 (`run-2@20261128-071526`, sau cải tiến):** đạt **20/22 (91%)** (`thuong 8/8`, `kho 9/11`, `tu_choi 3/3`, `0%` bịa mã ngoài `data/lesson.json`) ([eval/run-2.csv](eval/run-2.csv), chi tiết ở [eval/report.md](eval/report.md) và [eval/README.md](eval/README.md)).
Dữ liệu bài giảng là 15 đoạn tóm tắt có kiểm soát (`data/lesson.json`), chưa kết nối trực tiếp DB LMS thật.
Hướng dẫn chi tiết: [Nối model](docs/connect-model.md).

Trình tự vận hành: `python run.py eval --try` → `python run.py eval` →
người duyệt chấm `pass` → `python run.py score eval/run-1.csv` (và `eval/run-2.csv`).
Đã chạy thử 10 phiên và đo mô phỏng chính thức 50 phiên (`simulate-2@20261128-071851`, tỷ lệ đạt `20/22 = 90.9%`): chi phí trung bình **$0.0013/phiên**, **$0.0014/task thành công**, kịch bản cơ sở (`213` học viên) tốn **$1.65/tháng** (**$0.0078/người/tháng**), chi tiết tại [báo cáo chi phí](cost/cost-estimate.md).

Demo trực tiếp bằng giao diện Web (`python demo/demo_server.py` tại `http://127.0.0.1:8765`) hoặc dòng lệnh (`python run.py`): dùng tình huống thường `C02` (nhầm khái niệm Chatbot vs LLM → gợi ý xem lại `d01-chatbot-la-ung-dung`), tình huống khó `C05`/`C06` (hỏi ngoài bài / trả lời cụt `"ok"`), và tình huống tấn công `C11` (Prompt Injection đòi chấm 10/10 và mở khóa video → chặn 0-token).

## Bảy hạng mục bắt buộc — nằm ở file nào

| # | Hạng mục | File |
|---|---|---|
| 1 | Bằng chứng pain | `evidence/` (tổng hợp ở `evidence/summary.md`) |
| 2 | Impact có số | `spec.md` §2 |
| 3 | Thiết kế giải pháp | `spec.md` §4 |
| 4 | Bản chạy thử làm trọn lát cắt | `codebase/` · lệnh ở mục "Lệnh" |
| 5 | Định nghĩa "tốt" + bộ câu thử | `data/DATA_CARD.md` · `eval/` |
| 6 | Mô phỏng chi phí khi dùng thật | `cost/` |
| 7 | Slide + demo + video dự phòng | `demo-slides.pdf` ở thư mục gốc · link video: https://drive.google.com/file/d/19x3vtQ9bLlrmBqUgI2M6JGAe-Fjatyc7/view?usp=sharing |
| + | *Bonus:* người dùng thử | `validation/log.md` |
