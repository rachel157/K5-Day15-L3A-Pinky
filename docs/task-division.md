# Phân công công việc & Hướng dẫn thực hiện — Nhóm Pinky (L3A · Track A)

> Bài toán: **Checkpoint Tutor** (xem `canvas.md`).  
> Mốc gần nhất: **CP2 — 19:30 Thứ Sáu 27/11** · **CP3 — 10:00 Thứ Bảy 28/11** · **CP4 — 14:30 Thứ Bảy 28/11** · **Chốt cuối — 23:59 Thứ Bảy 28/11**.

---

## 1. Đội hình & vai trò chính

| Thành viên | Mã HV | Vai trò | Trọng tâm phụ trách |
|---|---|---|---|
| **Phạm Việt Hưng** | `2A202603370` | Đội trưởng / Dev | Điều phối tiến độ, chốt `canvas.md` & `spec.md`, phụ trách `data/DATA_CARD.md`, theo sát bằng chứng pain & nộp checkpoint |
| **Phạm Nguyên Vũ** | `2A202603436` | Thành viên / DevOps | Môi trường chạy, quản lý `.env`/API key, nối model trong `codebase/ai.py`, chạy thử `eval`/`simulate`, chuẩn bị máy demo & video dự phòng |
| **Chu Mai Hồng** | `2A202603377` | Thành viên / BA | Nghiên cứu người dùng (phỏng vấn, `evidence/`), đặc tả pain & kịch bản khó (`spec.md` §5), xây `eval/benchmark.csv` & `eval/metric_spec.yaml` |
| **Nguyễn Hoàng Tùng** | `2A202603481` | Thành viên / Dev | Thiết kế & code Agent (`codebase/agent.py`, `codebase/tools.py`): chia đoạn transcript, tạo câu hỏi checkpoint, đánh giá câu trả lời & đề xuất xem lại kèm mã đoạn |

---

## 2. Hướng dẫn chi tiết cho Checkpoint 2 (17:00 → 19:30 Thứ Sáu 27/11)

> **Lưu ý quan trọng:** Sau **19:30**, chuẩn **"đạt"** (`spec.md` §7) và `eval/metric_spec.yaml` được chốt cố định. Mọi thay đổi sau CP2 phải ghi vào changelog (`spec.md` §10).

### Bước 1 — Cả nhóm tổng hợp pain (20 phút · 17:05 – 17:25)
Cả 4 người ngồi chung, không tách nhóm:
- [ ] **Chu Mai Hồng (dẫn chính):** Chốt giả thuyết pain vào `evidence/hypothesis.md` và bộ câu hỏi phỏng vấn (`evidence/interviews/TEMPLATE.md`).
- [ ] **Cả nhóm:** Rà nhanh dữ liệu BTC cấp trong `data/preclass` (nếu có) xem có log xem lại/bỏ dở video hay bài giảng mẫu để trích đoạn không *(chỉ ghi kết quả đếm vào `evidence/data-mining.md`, không commit file data gốc)*.
- [ ] **Phạm Việt Hưng + Chu Mai Hồng:** Chốt lịch hẹn phỏng vấn ≥ 3 học viên L3A ngoài nhóm và ghi vào bảng *Lịch hẹn* cuối file `evidence/summary.md` (chỉ ghi vai + giờ, không ghi tên thật). Nếu phỏng vấn nhanh được ngay 1–2 người tại lớp thì ghi luôn số đầu tiên + 1 trích dẫn.

### Bước 2 — Cả nhóm cùng chốt lát cắt & sơ đồ (25 phút · 17:25 – 17:50)
- [ ] Chốt **Lát cắt một câu** (1 người dùng · 1 việc · 1 quyết định AI · 1 kết quả) cho **Checkpoint Tutor**:
  - *Input của `answer(text)` là gì?* (VD: mã bài/đoạn transcript + câu hỏi checkpoint + câu trả lời của học viên, hoặc học viên gửi câu trả lời cho một checkpoint cụ thể).
  - *Output trả về có cấu trúc gì?* (VD: nhận xét ngắn + quyết định `xem tiếp` hay `đề xuất xem lại` + mã đoạn cần xem lại kèm lý do + nhắc học viên vẫn có quyền xem tiếp).
- [ ] Vẽ **sơ đồ luồng** (workflow cố định hay 1 agent) và chốt danh sách công cụ (`@tool`) trong `spec.md` §4.
- [ ] Chốt **ranh giới AI** (không khóa video, không ép xem lại, không chấm điểm chính thức; khi thiếu căn cứ trong transcript phải nói rõ không có).
- [ ] Thống nhất sơ bộ **4 lớp chỗ khó** (`spec.md` §5) và **chuẩn "đạt"** (`spec.md` §7) để hai cặp làm không lệch nhau.

### Bước 3 — Tách 2 cặp làm song song (60 phút · 17:50 – 18:50)

#### Cặp X — Dựng khung `codebase/` + Nối API gọi thử 1 câu AI thật
**Thành viên:** **Nguyễn Hoàng Tùng** (lead luồng Agent) + **Phạm Nguyên Vũ** (lead môi trường & nối model)

| Người | Đầu việc cụ thể | File tác động | Đầu ra cần xong |
|---|---|---|---|
| **Nguyễn Hoàng Tùng** | Định nghĩa các công cụ `@tool` (trả dữ liệu mẫu từ `data/` trước) với đủ 4 ý docstring (`tên · input · output · tác động ra ngoài`) | `codebase/tools.py` | Các tool tra cứu đoạn transcript/checkpoint chạy được, không tác động ra ngoài |
| **Nguyễn Hoàng Tùng** | Viết luồng `answer(text) -> {"output": str}` đúng sơ đồ `spec.md` §4 và khung `SYSTEM` prompt | `codebase/agent.py` | Chạy `python run.py` đi hết luồng từ input → tool → `call_model` → output |
| **Phạm Nguyên Vũ** | Tạo `.env` từ `.env.example`, lấy API key (OpenAI / Gemini / Claude… theo `docs/connect-model.md`) | `.env` *(chỉ giữ trên máy, không commit)* | Có sẵn API key hoạt động |
| **Phạm Nguyên Vũ** | Viết nhánh gọi model thật trong `call_model(system, user)` trả đúng 4 khoá (`text`, `model`, `tokens_in`, `tokens_out` từ `usage` của API) | `codebase/ai.py`, `requirements.txt` *(nếu thêm thư viện)* | Gọi được **≥ 1 câu AI thật** (`tokens_in > 0`, `tokens_out > 0`) qua `python run.py` hoặc `python run.py eval --try 1` |

#### Cặp Y — `data/DATA_CARD.md` + ≥ 10 câu thử + `eval/metric_spec.yaml` + Chốt CP2
**Thành viên:** **Chu Mai Hồng** (lead bộ câu thử & metric) + **Phạm Việt Hưng** (lead Data Card, Canvas & chuẩn "đạt")

| Người | Đầu việc cụ thể | File tác động | Đầu ra cần xong |
|---|---|---|---|
| **Chu Mai Hồng** | Xây **≥ 10 câu thử** (xoá 3 dòng mẫu `B01`–`B03`), đủ 6 cột (`id,input,expected,pass_criterion,type,source`): gồm câu `thuong`, `kho` (hướng tới ≥ 5 câu phủ 4 lớp chỗ khó), và ≥ 2 câu `tu_choi` (gồm **2 câu tấn công**); ≥ 1/3 câu từ `nguoi_dung` / `data_that` | `eval/benchmark.csv` | File CSV UTF-8 hợp lệ, ≥ 10 câu thực tế của Checkpoint Tutor |
| **Chu Mai Hồng** | Điền đầy đủ **≥ 3 metric** (`name`, `definition`, `grader`, `threshold`), xoá mẫu `<metric_1>`… | `eval/metric_spec.yaml` | Đủ ≥ 3 metric đo được, rõ tiêu chí đạt/trượt |
| **Phạm Việt Hưng** | Viết bản đầu Data Card (mô tả dataset mẫu/trích đoạn transcript dùng cho tool & bộ câu thử, nguồn, bước xử lý, giới hạn) | `data/DATA_CARD.md` | Đủ mục Dataset 1 cho CP2 |
| **Phạm Việt Hưng** | Chốt **Chuẩn "đạt"** ở `spec.md` §7, điền mục 1–4 của `eval/README.md`, cập nhật `canvas.md` (dòng 4 số bằng chứng đầu nếu có + dòng *"Đã đổi gì so với CP1"*) | `spec.md`, `eval/README.md`, `canvas.md` | Chuẩn "đạt" chốt rõ ràng, khớp với `metric_spec.yaml` |

### Bước 4 — Đổi chéo review & Kiểm tra trước 19:30 (40 phút · 18:50 – 19:30)

1. **Đổi chéo review (20 phút · 18:50 – 19:10):**
   - **Cặp X review bài của Cặp Y:**
     - [ ] Kiểm tra ô `input` trong `eval/benchmark.csv` có khớp đúng định dạng đầu vào mà `answer(text)` đang nhận không.
     - [ ] Đọc `eval/metric_spec.yaml` và `spec.md` §7 xem tiêu chí chấm có mơ hồ không (người không viết spec có chấm giống người viết không).
     - [ ] Kiểm tra `data/DATA_CARD.md` khớp với dữ liệu thực tế `tools.py` đang đọc.
   - **Cặp Y review bài của Cặp X:**
     - [ ] Chạy thử `python run.py` với vài tình huống thật (trả lời đúng, trả lời sai/lệch ý chính, hỏi ngoài bài học).
     - [ ] Kiểm tra Agent có tuân thủ ranh giới không (chỉ **đề xuất** xem lại kèm mã đoạn, không khóa video, không chấm điểm chính thức, không bịa nội dung ngoài transcript).

2. **Chốt kỹ thuật & kiểm tra bắt buộc trước khi rời lớp 19:30 (20 phút · 19:10 – 19:30):**
   - [ ] **Phạm Nguyên Vũ:** Xác nhận đã gọi thành công **ít nhất 1 câu AI thật** với API key (thấy `tokens_in > 0`, `tokens_out > 0`), và lưu lại hướng dẫn ngắn cách tạo `.env` để sáng Thứ Bảy các bạn ở nhà chạy được ngay.
   - [ ] **Phạm Nguyên Vũ:** Chạy `git status` kiểm tra **tuyệt đối không có file `.env`, API key hay file data gốc BTC** trong commit.
   - [ ] **Phạm Việt Hưng:** Chạy lệnh kiểm tra tự động:
     ```powershell
     python run.py check
     ```
     Đảm bảo:
     - `TEAMS.md`: không có cảnh báo.
     - `eval/benchmark.csv`: ≥ 10 câu, không còn dòng mẫu `B01`–`B03`, đủ ≥ 2 câu `tu_choi` (gồm 2 câu tấn công), ≥ 1/3 câu từ `nguoi_dung`/`data_that`.
     - `eval/metric_spec.yaml`: ≥ 3 metric điền đủ 4 trường.
   - [ ] **Cả nhóm:** Merge/commit sạch lên nhánh `main` và push lên remote.
   - [ ] **Phạm Việt Hưng (`2A202603370`):** Nộp CP2 trước 19:30.

---

## 3. Lộ trình phân công sau CP2 (CP3 → CP4 → Chốt cuối)

### Chặng CP3 — Trước 10:00 Thứ Bảy 28/11 *(làm từ xa, không có lớp sáng Thứ Bảy)*

| Thành viên | Nhiệm vụ chính | File / Lệnh đầu ra |
|---|---|---|
| **Chu Mai Hồng** | Hoàn tất phỏng vấn ≥ 3 học viên L3A (`evidence/interviews/P1.md`…`P3.md`), tổng hợp `evidence/summary.md`; mở rộng `eval/benchmark.csv` lên **20–30 câu** (giữ nguyên chuẩn "đạt" & metric đã chốt) | `evidence/`, `eval/benchmark.csv` |
| **Phạm Việt Hưng** | Hoàn thiện `spec.md` §0–§7 (luồng hiện tại, bảng Impact §2, giải pháp tương tự §3, thiết kế §4, 4 lớp chỗ khó §5, 4 đường đi §6) và cập nhật `data/DATA_CARD.md` đầy đủ | `spec.md`, `data/DATA_CARD.md` |
| **Nguyễn Hoàng Tùng** | Hoàn thiện prompt, logic chia đoạn transcript, câu hỏi checkpoint & đề xuất xem lại trong `codebase/agent.py`, `codebase/tools.py` | `codebase/agent.py`, `codebase/tools.py` |
| **Phạm Nguyên Vũ** | Chạy `python run.py eval --try` (xác nhận nối model thật) → chạy `python run.py eval` ra **lượt 1** (`eval/run-1.csv` + `traces/run-1.jsonl`); dựng khung `cost/personas.yaml` và chạy thử `python run.py simulate --try` (10 phiên) | `eval/run-1.csv`, `cost/personas.yaml`, `cost/simulate-try.csv` |

### Chặng CP4 — Trước 14:30 Thứ Bảy 28/11

| Thành viên | Nhiệm vụ chính | File / Lệnh đầu ra |
|---|---|---|
| **Chu Mai Hồng + Phạm Việt Hưng** | Chấm cột `pass` cho `eval/run-1.csv` (có người thứ 2 chấm chéo 5 câu kiểm khớp ≥ 4/5) → `python run.py score eval/run-1.csv`; phân tích nhóm lỗi chính; ghi `validation/log.md` *(nếu kịp cho người dùng thử bonus)* | `eval/run-1.csv`, `eval/report.md`, `validation/log.md` |
| **Nguyễn Hoàng Tùng** | Cải tiến Agent dựa trên nhóm lỗi lớn nhất của lượt 1 (ghi lý do vào `spec.md` §10 changelog) | `codebase/agent.py`, `codebase/tools.py`, `spec.md` §10 |
| **Phạm Nguyên Vũ** | Chạy **lượt 2** (`python run.py eval` → `eval/run-2.csv`), chấm `score`, sau đó chạy mô phỏng chi phí đủ ≥ 50 phiên (`python run.py simulate --rate-from eval/run-2.csv`) và điền `cost/cost-estimate.md`, `spec.md` §8; chuẩn bị máy demo + quay **video dự phòng** | `eval/run-2.csv`, `cost/simulate-1.csv`, `cost/cost-estimate.md`, video dự phòng |
| **Phạm Việt Hưng + Cả nhóm** | Hoàn thiện `spec.md` §8–§10, `eval/README.md` mục 5–6, `README.md`, `docs/ai-usage.md`; làm slide theo `slides/outline.md` → xuất **`demo-slides.pdf`** ở thư mục gốc và chia phần thuyết trình (mỗi người ≥ 1 phần) | `spec.md`, `demo-slides.pdf`, `README.md`, `docs/ai-usage.md` |

### Chốt cuối — Trước 23:59 Thứ Bảy 28/11
- [ ] **Cả 4 thành viên:** Mỗi người viết 1 file reflection riêng từ `reflection/TEMPLATE.md` → `reflection/<ten>.md`.
- [ ] **Phạm Việt Hưng:** Cập nhật `spec.md` §10 (mục *Sau CP4*) nếu có chỉnh sửa theo góp ý sau demo, rà lại toàn bộ repo và push bản cuối.

---

## 4. Quy tắc phối hợp & Luật không được vi phạm

1. **Không sửa file khung:** `codebase/tracing.py`, `eval/run_eval.py`, `cost/simulate.py`, `run.py`.
2. **Bảo mật & dữ liệu:** Tuyệt đối không commit `.env`, API key, dữ liệu cá nhân thật hay nguyên file data BTC cấp (`data/preclass`).
3. **Tính trung thực sau CP2:** Không sửa chuẩn "đạt" (`spec.md` §7) và `eval/metric_spec.yaml` sau 19:30 Thứ Sáu; không xoá câu thử trượt, không sửa `expected` để khớp output, không sửa tay `eval/run-*.csv`, `cost/simulate-*.csv`, `traces/*` (trừ điền cột `pass`, `ghi_chu`).
4. **Quy ước Git nhanh:** Trước khi làm việc mới luôn `git pull`; chia file theo cặp để tránh conflict; mọi thay đổi lớn sau CP2 đều ghi 1 dòng vào `spec.md` §10.
