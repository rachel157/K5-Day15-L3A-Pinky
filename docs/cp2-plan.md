# Kế hoạch & Phân công Checkpoint 2 — Nhóm Pinky (L3A · Track A)

> **Hạn chót:** **19:30 Thứ Sáu 27/11** (**4 điểm** — đúng hạn + đủ 6 hạng mục; muộn/thiếu = **0 điểm**).  
> **Người nộp form thay cả nhóm:** **Phạm Việt Hưng (`2A202603370`)**.  
> **Lưu ý sống còn:** Chuẩn **"đạt"** (`spec.md` §7) và `eval/metric_spec.yaml` phải **chốt & commit trước 19:30** và **tuyệt đối không sửa sau CP2** (sửa sau sẽ bị 0 điểm khối R4).

---

## 1. Bảng phân công tổng thể 4 thành viên cho CP2

| Thành viên | Mã HV | Vai trò | Cặp | Các file & đầu việc chịu trách nhiệm chính ở CP2 |
|---|---|---|---|---|
| **Phạm Việt Hưng** | `2A202603370` | Đội trưởng / Dev | **Cặp Y** | Cập nhật `canvas.md` (CP2), `spec.md` (§3, §4 cùng Tùng, chốt §7 chuẩn "đạt"), `data/DATA_CARD.md`, `eval/README.md` (mục 1–4 + kết quả chấm chéo 5 output), chạy `python run.py check` & **nộp CP2** |
| **Chu Mai Hồng** | `2A202603377` | BA | **Cặp Y** | Viết `evidence/hypothesis.md`, ghi số đào data vào `evidence/data-mining.md` (từ `evidence/count.py`), đặt lịch / ghi `evidence/summary.md` & `evidence/interviews/P1.md`…, điền `spec.md` §5, viết ≥ 10 câu thử `eval/benchmark.csv` & ≥ 3 metric `eval/metric_spec.yaml` |
| **Nguyễn Hoàng Tùng** | `2A202603481` | Dev (Agent) | **Cặp X** | Dựng khung `codebase/tools.py` (`@tool` + dữ liệu giả lập mẫu) & `codebase/agent.py` (`answer(text)` đi hết luồng theo sơ đồ), cùng Hưng chốt sơ đồ & chỗ chặn rủi ro ở `spec.md` §4 |
| **Phạm Nguyên Vũ** | `2A202603436` | DevOps | **Cặp X** | Kiểm thử `python run.py` chế độ giả, chấm thử 5 output (đối chiếu với Hồng ≥ 4/5), lấy API key tạo `.env` (không commit), nối thử model trong `codebase/ai.py` và **gọi thành công ≥ 1 câu AI thật trước khi rời lớp 19:30** |

---

## 2. Lịch chạy nước rút (17:40 → 19:30 · 110 phút)

### Giai đoạn A — Cả nhóm tổng hợp pain (20 phút · 17:40 – 18:00)
*Làm chung cả 4 người, tận dụng kết quả đã chạy sẵn từ `evidence/count.py` trên `data/preclass`:*

- [ ] **Hồng (dẫn chính):** Chốt nhanh `evidence/hypothesis.md` (ghi rõ giả thuyết trước khi tiếp tục thu thêm phỏng vấn).
- [ ] **Hồng + Hưng:** Đưa con số thật đã chạy từ `python evidence/count.py` vào `evidence/data-mining.md` làm bằng chứng đào data ban đầu:
  - `2.602/4.322 (60.2%)` lượt tua video là **tua lùi** (`177/431 = 41.1%` học viên xem video từng tua lùi).
  - `213/431 (49.4%)` học viên mở lại cùng video ≥ 2 lần (`39.7%` từng xem tới cuối video).
  - `399/1.968 (20.3%)` lượt làm kiểm tra sau học (`pre_post_post`) **sai ngay lần đầu** (`69/77 = 89.6%` học viên từng sai).
  - Kèm ≥ 5 dòng ví dụ ẩn danh (`L0006`, `L0503`, `L0379`, `L0213`, `L0057`…) mà `evidence/count.py` đã in sẵn.
- [ ] **Cả nhóm (4 người):** Trong giờ giải lao / tại lớp, **mỗi người hẹn hoặc hỏi nhanh ít nhất 1 bạn học viên L3A/L3B ngoài nhóm** (lấy ≥ 1 trích dẫn thật cho `canvas.md` và ghi lịch hẹn / tiến độ vào `evidence/summary.md`).

### Giai đoạn B — Cả nhóm chốt lát cắt, sơ đồ & chuẩn "đạt" (20 phút · 18:00 – 18:20)
*Ngồi chung chốt khung thiết kế để Cặp X và Cặp Y không làm lệch format của nhau:*

- [ ] **Chốt lát cắt 1 câu** (dựa trên pain thật vừa tổng hợp) để cập nhật `canvas.md` và `spec.md` §4.
- [ ] **Chốt định dạng `input` / `output` của `answer(text)`:**
  - *Input mẫu:* mã bài/đoạn hoặc ngữ cảnh câu hỏi checkpoint + câu trả lời của học viên.
  - *Output mẫu:* nhận xét ngắn + quyết định (`xem tiếp` hoặc `đề xuất xem lại` kèm mã đoạn `[...]` + lý do) + giữ quyền học viên tự chọn xem tiếp.
- [ ] **Chốt hình dạng & công cụ (`spec.md` §4):**
  - Hình dạng: **Workflow cố định** (tra đoạn bài → đánh giá câu trả lời → xuất đề xuất kèm mã đoạn) — ghi rõ lý do vì sao **không** chọn 1 agent vòng lặp hay nhiều agent (việc lặp lại, dễ đo, rẻ token, không bị lạc bước).
  - Công cụ (`@tool`): ví dụ `get_lesson_segments(lesson_id)` / `search_segment(query)` (chỉ đọc, không tác động ra ngoài).
  - Chỗ chặn rủi ro & người duyệt: không khóa video, không ép tua lại, không chấm điểm chính thức; giảng viên duyệt nội dung/câu hỏi; thiếu căn cứ trong đoạn bài thì nói rõ *"không có trong bài"*.
- [ ] **Thống nhất khung chuẩn "đạt"** (`spec.md` §7) và **3 metric** (`eval/metric_spec.yaml`) để Cặp Y hoàn thiện.

---

### Giai đoạn C — Tách 2 cặp làm song song (40 phút · 18:20 – 19:00)

#### Cặp X — Khung `codebase/` + Chạy luồng AI giả + Chuẩn bị gọi AI thật
**Thành viên:** **Nguyễn Hoàng Tùng** + **Phạm Nguyên Vũ**

| Người | Việc cụ thể cần làm xong | File |
|---|---|---|
| **Nguyễn Hoàng Tùng** | Tạo dữ liệu mẫu nhỏ (trích đoạn bài ngắn giả lập / ẩn danh) và viết công cụ `@tool` đọc đoạn bài trong `codebase/tools.py` (đủ docstring 4 ý: *tên · input · output · tác động ra ngoài*) | `codebase/tools.py`, `data/` *(chỉ mẫu nhỏ)* |
| **Nguyễn Hoàng Tùng** | Viết `SYSTEM` prompt và luồng `answer(text) -> {"output": str}` trong `codebase/agent.py` đúng sơ đồ đã chốt ở `spec.md` §4 | `codebase/agent.py` |
| **Nguyễn Hoàng Tùng** | Hoàn thiện bảng công cụ, mức tự động, ≥ 3 nguyên tắc thiết kế (bắt buộc **G10**) và ghi rõ phần nào đang dùng giả vào `spec.md` §4 | `spec.md` §4 |
| **Phạm Nguyên Vũ** | Chạy kiểm tra khung bằng `python run.py` (chế độ AI giả `MODEL_PROVIDER=fake`) đảm bảo đi hết luồng không lỗi; kiểm tra `python run.py eval --fake` | `codebase/app.py`, `README.md` *(ghi lệnh chạy nếu có bổ sung)* |
| **Phạm Nguyên Vũ** | Tạo file `.env` từ `.env.example`, lấy API key (theo `docs/connect-model.md`), chuẩn bị nhánh gọi model thật trong `codebase/ai.py` (ưu tiên giữ được chế độ `fake` khi chưa bật key để CP2 chạy sạch, và test gọi riêng ≥ 1 câu AI thật) | `.env` *(không commit)*, `codebase/ai.py` |

#### Cặp Y — Bằng chứng + Thiết kế §3/§5/§7 + Data Card + 10 câu thử + Metric
**Thành viên:** **Chu Mai Hồng** + **Phạm Việt Hưng**

| Người | Việc cụ thể cần làm xong | File |
|---|---|---|
| **Chu Mai Hồng** | Hoàn thiện `evidence/hypothesis.md`, `evidence/data-mining.md` (số từ `count.py`), cập nhật tiến độ phỏng vấn + bảng lịch hẹn vào `evidence/summary.md` (và `P1.md` nếu đã hỏi xong 1 người) | `evidence/hypothesis.md`, `evidence/data-mining.md`, `evidence/summary.md` |
| **Chu Mai Hồng** | Điền `spec.md` §5: cụ thể hoá **4 lớp chỗ khó** thành **≥ 6 kịch bản + 2 kịch bản tấn công** nhắm vào chỗ chặn rủi ro (đòi chấm 10 điểm chính thức / mở khóa video / giải hộ mini lab / prompt injection) | `spec.md` §5 |
| **Chu Mai Hồng** | Viết **≥ 10 câu thử** trong `eval/benchmark.csv` (xoá 3 dòng mẫu `B01`–`B03`), đủ 6 cột `id,input,expected,pass_criterion,type,source`; có câu `thuong`, `kho`, và ≥ 2 `tu_choi` (gồm 2 câu tấn công); ≥ 1/3 câu từ `data_that` hoặc `nguoi_dung` | `eval/benchmark.csv` |
| **Chu Mai Hồng** | Điền **≥ 3 metric** kiểm chứng được (`name`, `definition`, `grader`, `threshold`, `why`) vào `eval/metric_spec.yaml` | `eval/metric_spec.yaml` |
| **Phạm Việt Hưng** | Cập nhật `canvas.md`: điền số bằng chứng đầu tiên + 1 trích dẫn (từ `data/preclass` / phỏng vấn đầu), chốt lát cắt 1 câu và ghi 1–3 dòng **"Đã đổi gì so với CP1"** | `canvas.md` |
| **Phạm Việt Hưng** | Điền `spec.md` §3 (3–4 dòng giải pháp tương tự: đáng học · đáng né · mình khác gì) và viết bản đầu `data/DATA_CARD.md` (mô tả nguồn dữ liệu mẫu + `data/preclass` đã xử lý thế nào) | `spec.md` §3, `data/DATA_CARD.md` |
| **Phạm Việt Hưng** | Chốt **Chuẩn "đạt"** bằng số vào `spec.md` §7 (VD: *"Đạt khi ≥ 80% câu qua, và 100% câu `tu_choi` qua"*) và điền mục 1–4 của `eval/README.md` | `spec.md` §7, `eval/README.md` |

---

### Giai đoạn D — Đổi chéo review, chấm thử 5 output & test 1 câu AI thật (30 phút · 19:00 – 19:30)

1. **Đổi chéo review (15 phút · 19:00 – 19:15):**
   - **Cặp X review bài Cặp Y:**
     - **Tùng** kiểm tra `input` trong `eval/benchmark.csv` có khớp đúng định dạng `answer(text)` đang nhận không.
     - **Vũ** (đóng vai người thứ hai không viết spec) đọc `eval/metric_spec.yaml` và **chấm độc lập 5 output mẫu** → đối chiếu với **Hồng**, phải khớp **≥ 4/5** (nếu lệch ≥ 2/5 thì sửa lại câu chữ `definition` ngay trước 19:30). Ghi kết quả khớp `__/5` vào `eval/README.md` mục 3.
   - **Cặp Y review bài Cặp X:**
     - **Hồng + Hưng** chạy thử `python run.py` kiểm tra luồng đi từ input → tool → `call_model` → output có khớp sơ đồ `spec.md` §4 và giữ đúng ranh giới an toàn không.

2. **Test AI thật trước khi rời lớp + Kiểm tra trước nộp (15 phút · 19:15 – 19:30):**
   - [ ] **Vũ:** Bật API key trong `.env`, chạy thử gọi **≥ 1 câu AI thật** (`python run.py` hoặc `python run.py eval --try 1`) thấy trả về câu trả lời thật và `tokens_in > 0`, `tokens_out > 0`. Ghi chú ngắn cho nhóm cách tạo `.env` để sáng Thứ Bảy ở nhà chạy được ngay.
   - [ ] **Vũ:** Chạy `git status` kiểm tra **tuyệt đối không có `.env`, API key hay file data gốc của BTC**.
   - [ ] **Hưng:** Chạy lệnh kiểm tra bắt buộc:
     ```powershell
     python run.py check
     ```
     Đảm bảo không còn lỗi/cảnh báo chặn CP2 (`TEAMS.md` sạch, `benchmark.csv` ≥ 10 câu không còn `B01`–`B03`, đủ ≥ 2 `tu_choi`, ≥ 1/3 nguồn thật/người dùng, `metric_spec.yaml` đủ ≥ 3 metric).
   - [ ] **Cả nhóm:** Commit + push sạch lên nhánh `main` trước **19:25**.
   - [ ] **Hưng (`2A202603370`):** Điền form nộp CP2 trước **19:30**.

---

## 3. Checklist 6 việc bắt buộc phải có trên repo trước 19:30

- [ ] **1. `canvas.md`:** Có số bằng chứng đầu + 1 trích dẫn, lát cắt 1 câu, và mục *"Đã đổi gì so với CP1"*.
- [ ] **2. `evidence/`:** Có báo cáo nguồn đang làm & tiến độ (`evidence/hypothesis.md`, `evidence/data-mining.md` + `evidence/count.py`, lịch hẹn / kết quả đầu ở `evidence/summary.md`).
- [ ] **3. `spec.md` §3–§5:** Đủ giải pháp tương tự (§3), sơ đồ + hình dạng + công cụ + chặn rủi ro + người duyệt + mức tự động + ≥ 3 nguyên tắc gồm G10 + phần giả (§4), và ≥ 6 kịch bản + 2 tấn công (§5).
- [ ] **4. `eval/` & `data/`:** `eval/benchmark.csv` ≥ 10 câu đủ 6 cột, `eval/metric_spec.yaml` ≥ 3 metric (đã chấm thử chéo ≥ 4/5 ghi ở `eval/README.md`), `data/DATA_CARD.md` bản đầu.
- [ ] **5. `spec.md` §7:** Chốt chuẩn "đạt" bằng số và **không sửa sau 19:30**.
- [ ] **6. `codebase/`:** `python run.py` chạy hết luồng (chế độ giả/thật), `python run.py check` hợp lệ; đã test gọi thử được ≥ 1 câu AI thật trước khi rời lớp (không commit `.env`).
