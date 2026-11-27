# Tổng hợp bằng chứng pain

> Điền ở guide bước 1.2, xong trước **CP3 10:00 Thứ Bảy 28/11**. Chấm ở rubric R1.
> Ba nguồn ngang nhau — tối thiểu **≥1 nguồn đạt ngưỡng**. Mạnh nhất: đào data ra insight → hỏi người dùng để kiểm lại (hoặc ngược lại).

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | File |
|---|---|---|
| Đào data (x/N, %, cách đếm chạy lại được, ≥5 ví dụ) | ☑ | `evidence/data-mining.md` (+ `evidence/count.py`) |
| Phỏng vấn (≥3 người ngoài nhóm, đúng người dùng) | ☐ *(đang hẹn & triển khai)* | `evidence/interviews/P1.md`… |
| Khảo sát (≥20 người ngoài nhóm, đúng người dùng) | ☐ | `evidence/survey/` |

## 2. Số chính

- Đào data (`data/preclass`, Day01–Day13): `2.602/4.322 (60.2%)` lượt tua video là tua lùi (`177/431 = 41.1%` học viên mở video từng tua lùi); `213/431 (49.4%)` học viên mở lại cùng video ≥ 2 lần; `399/1.968 (20.3%)` lượt kiểm tra sau học sai ngay lần đầu (`69/77 = 89.6%` học viên làm phần này từng sai ít nhất 1 câu); `1.108/1.260 (87.9%)` lượt chat AI là hỏi dưới video/slide.
- Phỏng vấn: __/3 người gặp *(n nhỏ không ghi % · đang thực hiện cho CP3)* · số lần / tháng: P1 __, P2 __, P3 __ · mỗi lần mất __–__ phút
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
*(Sẽ bổ sung trích dẫn nguyên văn từ `P1`–`P3` sau khi hoàn thành phỏng vấn trước CP3).*

## 4. Các nguồn có khớp nhau không

Data nói: `60.2%` lượt tua là tua lùi, `49.4%` học viên mở lại video ≥ 2 lần và `89.6%` học viên từng sai lần đầu khi làm kiểm tra cuối ngày (`pre_post_post`). Người dùng nói: *(sẽ cập nhật đối chiếu sau khi phỏng vấn ≥ 3 học viên L3A ngoài nhóm trước CP3)*.

## 5. Kết luận

Giả thuyết ở `evidence/hypothesis.md`: **đang kiểm chứng thêm bằng phỏng vấn** — số đào data ban đầu ủng hộ chiều hướng học viên phải tua lùi/mở lại video nhiều và hay sai ở lần kiểm tra đầu tiên. Điều vẫn chưa biết: *vì sao* học viên vẫn sai sau khi xem video và cách tự tua lại gây bất tiện ở điểm nào (sẽ trả lời qua `P1`–`P3`).

## Lịch hẹn (dùng cho CP2 — chỉ ghi vai và giờ, không tên)

| Vai | Giờ hẹn | Đã xong? |
|---|---|---|
| Học viên L3A (ngoài nhóm) — P1 | *(điền giờ hẹn tối T6 / sáng T7)* | ☐ |
| Học viên L3A (ngoài nhóm) — P2 | *(điền giờ hẹn tối T6 / sáng T7)* | ☐ |
| Học viên L3A (ngoài nhóm) — P3 | *(điền giờ hẹn tối T6 / sáng T7)* | ☐ |
