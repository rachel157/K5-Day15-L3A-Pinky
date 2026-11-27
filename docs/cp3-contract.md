# Hợp đồng phối hợp CP3 → CP4

> Nhóm Pinky · L3A · Track A · Checkpoint Tutor
>
> Mục đích: thống nhất interface, phạm vi, quyền sở hữu file, thứ tự làm và điều kiện bàn giao để Code, Báo cáo, Evidence và DevOps có thể làm song song, không chờ nhau và không làm lệch sản phẩm.

## 1. Mục tiêu sản phẩm đã chốt

Checkpoint Tutor hỗ trợ học viên phát hiện lỗ hổng hiểu bài trong video và đề xuất đúng đoạn cần xem lại. Học viên luôn tự quyết định xem lại hay xem tiếp.

Agent không khóa video, không ép học viên xem lại, không tự chấm điểm chính thức, không sửa tiến độ học tập và không làm hộ bài nộp.

### 1.1. Lát cắt chính

> Một học viên xem video bài giảng và trả lời câu hỏi kiểm tra hiểu tại checkpoint; Agent đánh giá dấu hiệu hiểu bài, đề xuất xem lại đúng đoạn khi cần hoặc cho biết có thể xem tiếp, để học viên tự chọn hành động tiếp theo.

### 1.2. Phạm vi CP3–CP4

**Bắt buộc:**

- Agent nhận câu hỏi/câu trả lời checkpoint.
- Tìm đoạn bài học liên quan.
- Đánh giá câu trả lời theo căn cứ bài học.
- Đưa feedback ngắn.
- Đề xuất xem tiếp hoặc xem lại đúng mã đoạn.
- Từ chối đúng vai trò khi bị yêu cầu chấm điểm, mở khóa, sửa tiến độ hoặc làm hộ bài.
- Chạy được với model thật, có trace, token và run ID.
- Có lượt eval 1, cải tiến, lượt eval 2.

**Nếu còn thời gian, làm sau khi baseline chạy ổn:**

- Bài kiểm tra cuối video.
- Báo cáo tổng hợp các đoạn còn yếu.
- Giao diện video và nút tua đến timestamp.
- Sinh câu hỏi tự động từ transcript.
- Trạng thái câu hỏi `draft/reviewed/published`.

**Không được để các phần nâng cấp làm hỏng hoặc trì hoãn luồng checkpoint chính.** Deepgram, embedding, Qdrant và PostgreSQL là kiến trúc triển khai mở rộng, không phải dependency bắt buộc của CP3.

---

## 2. Hợp đồng dữ liệu và interface

### 2.1. Hàm bắt buộc

```python
answer(text: str) -> {"output": str}
```

- `text` là nguyên ô `input` trong `eval/benchmark.csv`.
- Output phải là dict có khóa `output` kiểu chuỗi.
- Không đổi chữ ký hàm nếu chưa được cả nhóm thống nhất.

### 2.2. Format input hiện tại

Benchmark đang dùng input tự nhiên, ví dụ:

```text
[Bài: Day01 AI LLM Foundation | Câu hỏi checkpoint: Chatbot khác gì với mô hình ngôn ngữ (LLM) thuần túy?] Học viên trả lời: Chatbot chính là mô hình LLM, không có khác biệt gì cả.
```

Agent phải tiếp tục hỗ trợ format này. Người học không cần biết hoặc tự nhập mã đoạn.

Có thể hỗ trợ thêm format debug nội bộ:

```text
mode=checkpoint
segment_id=d01-chatbot-la-ung-dung
question=Chatbot khác gì với LLM?
answer=Chatbot là lớp ứng dụng quanh model.
```

Nhưng format debug không được làm hỏng format benchmark tự nhiên.

### 2.3. Mã đoạn chuẩn

Code chỉ được trả mã tồn tại trong `data/lesson.json`. Danh sách mã hiện tại:

```text
d01-context-window
d01-chatbot-la-ung-dung
d01-chon-tang-model
d02-muc-tu-dong
d01-temperature
d01-system-user-prompt
d01-tri-nho-o-ung-dung
d01-ba-yeu-to-hoi-tu
d01-context-keep-table-clean
d01-bi-cat-giua-chung
d02-rule-workflow-agent
d02-cham-gate
d01-prompt-injection-safety
```

Nếu thêm hoặc đổi mã:

1. Người Code cập nhật `data/lesson.json`.
2. Gửi thông báo `[CODE UPDATE]` cho nhóm.
3. Người làm benchmark kiểm tra các câu và `pass_criterion` bị ảnh hưởng.
4. Người làm báo cáo cập nhật `spec.md`/Data Card nếu cần.
5. Không đổi mã sau khi đã chạy eval chính thức nếu không có lý do bắt buộc.

### 2.4. Hành động logic nội bộ

Output cuối là text, nhưng Code nên tư duy theo các nhánh:

| Nhánh | Ý nghĩa | Output tối thiểu |
|---|---|---|
| `continue` | Câu trả lời đủ ý | Xác nhận ngắn, cho biết có thể xem tiếp |
| `suggest_replay` | Sai, thiếu hoặc nhầm khái niệm | Chỉ ra lỗ hổng, mã đoạn, lý do, quyền xem tiếp |
| `ask_clarification` | Quá ngắn, mơ hồ hoặc né trả lời | Hỏi lại, không kết luận đã hiểu |
| `no_basis` | Không có căn cứ trong bài | Nói rõ không xác định được, không bịa mã đoạn |
| `refuse` | Vượt phạm vi/thẩm quyền | Từ chối đúng vai, không thực hiện tác động |

Không dùng các hành động `force_replay`, `block`, `fail_learner`.

### 2.5. Nội dung output bắt buộc

**Đúng:**

- Xác nhận đúng ý chính.
- Cho phép/khuyến khích xem tiếp.
- Không bắt xem lại.

**Sai/thiếu/nhầm:**

- Chỉ ra điểm sai hoặc ý còn thiếu.
- Đề xuất mã đoạn hợp lệ.
- Nêu lý do đoạn đó liên quan.
- Ghi rõ học viên vẫn có thể xem tiếp.

**Mơ hồ:**

- Không xác nhận đã hiểu.
- Hỏi lại hoặc yêu cầu nêu một ý chính.
- Không tự đoán mã đoạn khi chưa có căn cứ.

**Ngoài bài:**

- Nói rõ thông tin không có trong dữ liệu bài học hiện tại.
- Không bịa kiến thức hoặc mã đoạn.

**Vượt thẩm quyền/tấn công:**

- Không chấm điểm chính thức.
- Không mở khóa video.
- Không sửa `item_completed`/tiến độ.
- Không làm hộ bài mini lab để nộp.

---

## 3. Phần việc theo người

### 3.1. Nguyễn Hoàng Tùng — Code/Agent

**File sở hữu chính:**

- `codebase/agent.py`
- `codebase/tools.py`
- `data/lesson.json`
- Có thể thêm test nhỏ nếu cần

**Việc CP3:**

1. Ổn định input tự nhiên của benchmark.
2. Đảm bảo retrieval tìm đúng segment theo câu hỏi.
3. Đảm bảo mã đoạn trong output tồn tại trong data.
4. Xử lý đúng C01–C22 và các case tương tự, không hardcode nguyên câu benchmark.
5. Giữ quyết định an toàn bằng code; model không được tự chọn mã nguồn ngoài kết quả tool.
6. Duy trì fallback khi model lỗi hoặc output không đúng format.
7. Giữ output ngắn, phù hợp đọc tại điểm dừng video.
8. Thêm `final_quiz`/`review_report` chỉ sau khi checkpoint baseline ổn.
9. Phân tích lỗi sau run 1 và sửa nguyên nhân, không sửa `expected`.
10. Gửi thông báo thay đổi cho nhóm.

**Không làm:**

- Không sửa metric/threshold sau CP2.
- Không sửa `expected` để tăng pass.
- Không xóa câu thử bị trượt.
- Không commit `.env`/API key.
- Không tự đổi interface mà không báo nhóm.

**Tiêu chí hoàn thành Code:**

- `python run.py` chạy được.
- Model thật chạy được qua `call_model`.
- `python run.py eval` tạo run hợp lệ.
- Không lỗi runtime trong các case đã cam kết.
- Không bịa mã đoạn.
- Không ép xem lại.
- Không bị prompt injection điều khiển.

### 3.2. Phạm Việt Hưng — Báo cáo/điều phối

**File sở hữu chính:**

- `spec.md`
- `canvas.md`
- `README.md`
- `eval/README.md`
- `eval/report.md`
- `slides/outline.md`
- `data/DATA_CARD.md`
- Changelog `spec.md §10`

**Việc CP3:**

1. Hoàn thiện `spec.md §0–§7` theo bằng chứng và code thực tế.
2. Sửa bảng tool trong `spec.md §4` để khớp code:
   - `get_segment`
   - `search_segments`
   - `evaluate_answer`
   - `build_review_report`
3. Không để lại `search_example` nếu code không còn tool đó.
4. Hoàn thiện Data Card, phân biệt dữ liệu thật, tự dựng và tự ước tính.
5. Cập nhật Canvas CP2/CP3 theo số liệu thật.
6. Ghi run ID, kết quả và thay đổi vào báo cáo sau khi có run.
7. Chuẩn bị README, slide, kịch bản demo và giới hạn sản phẩm.
8. Tích hợp changelog từ thông báo Code, không tự đoán thay đổi kỹ thuật.

**Phần cần đợi run:**

- Kết quả eval lượt 1/lượt 2.
- Số token/model/chi phí.
- Danh sách lỗi thực tế.
- So sánh trước/sau cải tiến.

**Phần có thể làm ngay:**

- Bối cảnh hiện tại.
- Pain và bằng chứng.
- Impact.
- Thiết kế workflow.
- Rủi ro/an toàn.
- Roadmap Deepgram/embedding/Qdrant/PostgreSQL.
- Slide khung và README hướng dẫn chạy.

### 3.3. Chu Mai Hồng — BA/Evidence/Eval

**File sở hữu chính:**

- `evidence/`
- `eval/benchmark.csv` trước khi chạy eval chính thức
- Phối hợp đọc `eval/metric_spec.yaml` đã chốt

**Việc CP3:**

1. Hoàn thiện phỏng vấn tối thiểu 3 học viên ngoài nhóm.
2. Ghi P1/P2/P3 ẩn danh, không bịa trích dẫn.
3. Tổng hợp `evidence/summary.md` với ≥5 trích dẫn/ví dụ có nguồn.
4. Mở rộng benchmark trong phạm vi 20–30 câu nếu cần.
5. Chấm chéo 5 output với người thứ hai; mục tiêu khớp ≥4/5.
6. Không đổi metric/threshold sau CP2.
7. Nếu cần thêm câu benchmark, phải dùng mã đoạn có trong `lesson.json`.

### 3.4. Phạm Nguyên Vũ — DevOps/Model/Cost

**File sở hữu chính:**

- `codebase/ai.py`
- `requirements.txt` nếu thật sự cần
- `cost/`
- `eval/run-*.csv`, `traces/` do lệnh sinh ra
- Môi trường local và video dự phòng

**Việc CP3–CP4:**

1. Cấu hình `.env` local, tuyệt đối không commit.
2. Nối provider/model thật theo `docs/connect-model.md`.
3. Chạy `python run.py eval --try` và xác nhận token > 0.
4. Chạy eval lượt 1.
5. Sau khi Code cải tiến, chạy eval lượt 2.
6. Chạy mô phỏng chi phí đủ số phiên theo yêu cầu.
7. Cung cấp run ID, model, token, lỗi và file kết quả cho Hưng.
8. Kiểm tra máy demo và quay video dự phòng.

---

## 4. File ownership và quy tắc tránh conflict

### 4.1. Ai có thể sửa file nào

| File/thư mục | Chủ sở hữu chính | Người khác chỉ làm khi |
|---|---|---|
| `codebase/agent.py` | Tùng | Tùng yêu cầu review |
| `codebase/tools.py` | Tùng | Tùng yêu cầu review |
| `data/lesson.json` | Tùng | Thống nhất đổi mã/nội dung |
| `codebase/ai.py` | Vũ | Tùng cần thay đổi interface model |
| `spec.md` | Hưng | Người khác gửi nội dung, Hưng tích hợp |
| `canvas.md` | Hưng | Cả nhóm thống nhất số liệu |
| `evidence/` | Hồng | Hưng đọc để tổng hợp |
| `eval/benchmark.csv` | Hồng | Tùng xác nhận mã đoạn/input |
| `eval/metric_spec.yaml` | Đã chốt CP2 | Không sửa sau CP2 |
| `eval/README.md` | Hưng | Hồng cung cấp số liệu |
| `eval/report.md` | Hưng | Code/Vũ cung cấp run và lỗi |
| `cost/` | Vũ | Hưng cung cấp giả định người dùng |
| `README.md`, slide | Hưng | Mọi người gửi nội dung |

### 4.2. File không được sửa

Theo `AGENTS.md`, không sửa:

- `codebase/tracing.py`
- `eval/run_eval.py`
- `cost/simulate.py`
- `run.py`

Không sửa tay:

- `eval/run-*.csv`
- `cost/simulate-*.csv`
- `traces/*`

Ngoại lệ: điền cột `pass`/`ghi_chu` theo đúng quy trình chấm nếu được phép.

---

## 5. Phần làm ngay và phần phải đợi

### 5.1. Code có thể làm ngay

- Kiểm tra C01–C22 ở fake mode.
- Sửa retrieval và parser.
- Test mã đoạn hợp lệ.
- Test prompt injection/out-of-scope.
- Giữ output dưới giới hạn.
- Viết fallback.
- Thêm test cho `build_review_report`.
- Viết changelog đề xuất gửi Hưng.

### 5.2. Báo cáo có thể làm ngay

- Hoàn thiện §0–§6 dựa trên nội dung đã có.
- Hoàn thiện Data Card.
- Cập nhật bảng tool theo contract này.
- Hoàn thiện README/slide khung.
- Ghi roadmap nâng cấp.
- Chuẩn bị mẫu báo cáo eval.

### 5.3. Phải đợi model/run

- Điền kết quả lượt 1/lượt 2.
- Chấm pass thực tế.
- Phân tích lỗi chính dựa trên trace.
- Điền token/model/chi phí thật.
- Kết luận cải thiện trước/sau.

### 5.4. Phải thống nhất trước khi làm

- Đổi format input.
- Đổi/đổi tên mã đoạn.
- Thêm metric hoặc đổi threshold.
- Thêm thư viện ngoài.
- Dùng Deepgram/Qdrant/PostgreSQL trong luồng demo.
- Mở rộng thành nhiều agent.
- Sửa benchmark sau khi đã chạy eval chính thức.

---

## 6. Quy trình bàn giao

### 6.1. Thông báo Code

Mỗi thay đổi Code gửi vào nhóm theo mẫu:

```text
[CODE UPDATE]
Thay đổi:
File:
Input ảnh hưởng:
Output mong đợi:
Mã đoạn ảnh hưởng:
Benchmark ảnh hưởng:
Cách kiểm tra:
Changelog cần ghi:
```

### 6.2. Thông báo Run/DevOps

```text
[RUN RESULT]
Lệnh:
Run ID:
Model:
Tổng câu:
Pass/Fail:
Lỗi chính:
Tokens in/out:
File kết quả:
```

### 6.3. Thông báo Báo cáo

```text
[REPORT UPDATE]
File:
Đã cập nhật:
Nguồn:
Metric/section ảnh hưởng:
Cần Code xác nhận: Có/Không
```

### 6.4. Trước khi pull và làm việc

```powershell
git pull origin main
git status
```

Trước commit:

```powershell
git diff --check
python run.py check
git status --short
git diff --cached --name-only
```

---

## 7. Lộ trình CP3 → CP4

### Chặng A — Baseline

**Code:** test và ổn định Agent.

**Báo cáo:** hoàn thiện evidence/spec/Data Card độc lập.

**DevOps:** xác nhận model thật chạy được.

### Chặng B — Eval lượt 1

```powershell
python run.py eval
```

Sinh:

- `eval/run-1.csv`
- `traces/run-1.jsonl`

Không sửa tay output. Gửi run ID và lỗi cho Code/Báo cáo.

### Chặng C — Cải tiến

**Code:** sửa nguyên nhân lỗi lớn nhất, không sửa expected/metric.

**Báo cáo:** ghi lý do thay đổi vào `spec.md §10`, cập nhật `eval/report.md` sau khi có thông tin.

### Chặng D — Eval lượt 2 và đóng gói

```powershell
python run.py eval
python run.py score eval/run-2.csv
python run.py simulate --rate-from eval/run-2.csv
```

Sau đó hoàn thiện slide, README, chi phí, demo và video dự phòng.

---

## 8. Tiêu chí hoàn thành cuối

### Code

- [ ] `python run.py` chạy được.
- [ ] `python run.py eval` chạy được với model thật.
- [ ] Có run 1 và run 2 hợp lệ.
- [ ] Không có lỗi runtime không giải thích được.
- [ ] Câu đúng được cho xem tiếp.
- [ ] Câu sai/thiếu được đề xuất đúng đoạn.
- [ ] Câu mơ hồ không bị kết luận bừa.
- [ ] Câu ngoài bài không bị bịa.
- [ ] Câu tấn công không điều khiển Agent.
- [ ] Không khóa video/ép xem lại/chấm điểm chính thức.
- [ ] Mã đoạn trong output tồn tại trong dữ liệu.

### Báo cáo/evidence

- [ ] `spec.md §0–§10` đầy đủ theo mốc.
- [ ] Evidence có số liệu, mẫu số và nguồn.
- [ ] Có ít nhất 3 phỏng vấn phù hợp hoặc nguồn đạt ngưỡng rubric.
- [ ] Có ít nhất 5 trích dẫn/ví dụ có nguồn.
- [ ] Benchmark đạt số lượng CP yêu cầu.
- [ ] Metric và threshold giữ nguyên sau CP2.
- [ ] Có chấm chéo 5 output, khớp ≥4/5.
- [ ] Có kết quả run 1/run 2 và phân tích lỗi.
- [ ] Có token/model/chi phí.
- [ ] Có README, slide, demo dự phòng và roadmap.

---

## 9. Chốt trách nhiệm

> Tùng làm cho Agent chạy đúng theo hợp đồng và cải thiện theo lỗi eval. Hưng biến sản phẩm thành báo cáo có bằng chứng, số liệu và câu chuyện demo. Hồng cung cấp evidence và bộ câu thử. Vũ cung cấp model thật, run, trace và chi phí. Mỗi người bắt đầu phần độc lập ngay; chỉ dừng để thống nhất khi thay đổi interface, mã đoạn, metric hoặc phạm vi an toàn.
