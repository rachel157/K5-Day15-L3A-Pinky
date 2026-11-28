# Tổng hợp bằng chứng pain

> Điền ở guide bước 1.2, xong trước **CP3 10:00 Thứ Bảy 28/11**. Chấm ở rubric R1.
> Ba nguồn ngang nhau — tối thiểu **≥1 nguồn đạt ngưỡng**. Mạnh nhất: đào data ra insight → hỏi người dùng để kiểm lại (hoặc ngược lại).

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | File |
|---|---|---|
| Đào data (x/N, %, cách đếm chạy lại được, ≥5 ví dụ) | ☑ | `evidence/data-mining.md` (+ `evidence/count.py`) |
| Phỏng vấn (≥3 người ngoài nhóm, đúng người dùng) | ☐ *(chưa có ghi chép trong hồ sơ)* | `evidence/interviews/` |
| Khảo sát (≥20 người ngoài nhóm, đúng người dùng) | ☐ | `evidence/survey/` |

## 2. Số chính

- Đào data (`data/preclass`, Day01–Day13): `2.602/4.322 (60.2%)` lượt tua video là tua lùi (`177/431 = 41.1%` học viên mở video từng tua lùi); `213/431 (49.4%)` học viên mở lại cùng video ≥ 2 lần; `399/1.968 (20.3%)` lượt kiểm tra sau học sai ngay lần đầu (`69/77 = 89.6%` học viên làm phần này từng sai ít nhất 1 câu); `1.108/1.260 (87.9%)` lượt chat AI là hỏi dưới video/slide.
- Phỏng vấn: hồ sơ có lịch hẹn 3 học viên. Số buổi đã thực hiện, tần suất gặp khó và thời gian mỗi lần đang chờ ghi chép ẩn danh.
- Khảo sát: không dùng (tập trung đào data + phỏng vấn đối chiếu).

Phỏng vấn nhiều vai thì đếm theo từng vai, không cộng chung.

| | Vai | Gặp pain? | Số lần / 1 tháng qua | Lần gần nhất mất | Đang xoay xở bằng |
|---|---|---|---|---|---|
| P1 | | | | | |
| P2 | | | | | |
| P3 | | | | | |

## 3. ≥5 trích dẫn hoặc ví dụ nguyên văn (có nguồn, bỏ tên)

1. `events.csv:73` — `L0006` tua lùi video `d01-r1-v01` từ `88.9s -> 40.8s` (tìm lại đoạn giảng đã qua).
2. `events.csv:171-172` — `L0503` tua lùi 2 lần liên tiếp trong `d01-r1-v01` (`129.9s -> 118.8s -> 101.1s`).
3. `events.csv:195` — `L0503` đóng bỏ qua câu hỏi giữa video `day01-ai-llm-foundation:m01:s007` (`skipped_stop=True`).
4. `answers.csv:3` — `A00611` (`L0213`) trả lời sai ngay lần đầu câu kiểm tra `d01-on-chatbot-la-ung-dung` (`pre_post_post`, `lan_thu=1`).
5. `answers.csv:61` — `A00340` (`L0057`) trả lời sai ngay lần đầu bước thực hành `lab:d02-lab-chon-muc-giai-phap:chon-muc` (`thuc_hanh`, `lan_thu=1`).
Năm ví dụ trên lấy từ log hành vi và câu trả lời. Ghi chép phỏng vấn cần được bổ sung từ nguồn gốc đã ẩn danh.

## 4. Các nguồn có khớp nhau không

Data nói: `60.2%` lượt tua là tua lùi, `49.4%` học viên mở lại video ≥ 2 lần và `89.6%` học viên từng sai lần đầu khi làm kiểm tra cuối ngày (`pre_post_post`). Đối chiếu với lời kể của học viên đang chờ ghi chép `P1`–`P3`.

## 5. Kết luận

Log ủng hộ phần giả thuyết về hành vi tua lùi, mở lại video và sai lần đầu ở bài kiểm tra sau học. Lý do học viên tua lùi và mức bất tiện mỗi lần vẫn cần lời kể của học viên.

## Lịch hẹn (dùng cho CP2 — chỉ ghi vai và giờ, không tên)

| Vai | Giờ hẹn | Đã xong? |
|---|---|---|
| Học viên L3A (ngoài nhóm) — P1 | 18:30 Thứ Sáu 27/11 (trực tiếp tại lớp) | ☐ |
| Học viên L3A (ngoài nhóm) — P2 | 18:30 Thứ Sáu 27/11 (trực tiếp tại lớp) | ☐ |
| Học viên L3A (ngoài nhóm) — P3 | 18:30 Thứ Sáu 27/11 (trực tiếp tại lớp) | ☐ |
