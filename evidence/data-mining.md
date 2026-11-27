# Đào data — cách đếm và kết quả

> Điền ở guide bước 1.2. Ôn lại: ngày 2, ngày 6 · lab ngày 2, lab ngày 6.
> Không đào data thì xoá file này. Script / công thức đếm để trong repo (vd `evidence/count.py` hoặc ghi công thức Sheets ngay dưới), người khác chạy lại phải ra cùng số.
> Repo chỉ chứa số đã tổng hợp và vài dòng ví dụ — không chép lại nguyên file data.

## 1. Cách đếm — viết TRƯỚC khi chạy

- Data dùng: Bộ `data/preclass` do BTC cấp (nhật ký hành vi thật đã ẩn danh trên `preclass-online.com`, từ **05/11/2026 đến 25/11/2026**, Day01 → Day13), gồm `learners.csv`, `events.csv`, `answers.csv`, `chat.csv`.
- Đếm gì · trên tập nào · lọc gì:
  1. **Tỉ lệ lượt tua lùi video (`to < from`):** đếm trên toàn bộ sự kiện `type = video_seeked` trong `events.csv` (lọc các dòng có cả `from` và `to` là số).
  2. **Tỉ lệ học viên từng tua lùi / mở lại video ≥ 2 lần / xem hết video:** đếm trên tập học viên từng mở video (`type = video_opened`).
  3. **Tỉ lệ bỏ qua câu hỏi giữa video:** đếm các dòng `type = quiz_item_dismissed` có `data.skipped_stop == True` trên tổng số `quiz_item_dismissed`; và theo học viên trên tập học viên từng mở quiz (`quiz_item_opened`).
  4. **Tỉ lệ trả lời sai ngay lần đầu (`lan_thu = 1`):** lọc `answers.csv` với `lan_thu == 1` và `was_correct` khác rỗng (`True`/`False`), tách riêng theo `nguon` (`pre_post_post`, `thuc_hanh`, `video_quiz`).
  5. **Tỉ lệ hỏi trợ giảng AI dưới video/slide:** đếm `channel = video_question` trên tổng dòng `chat.csv` và trên tập học viên từng mở video.
- **Mẫu số là gì:**
  - Tổng tài khoản là `721` (`learners.csv`), nhưng chỉ có **`436` học viên có hoạt động** (`events.csv`) và **`431` học viên từng mở video** — dùng đúng mẫu số theo từng hành vi (không lấy `721` làm mẫu số chung cho mọi chỉ số).
  - Với tỉ lệ sai lần đầu ở `answers.csv`, mẫu số là số câu / số học viên **có làm và có chấm đúng/sai** ở `lan_thu = 1` (bỏ ô trống).
- Script chạy lại được: [`evidence/count.py`](evidence/count.py)  
  Lệnh chạy:
  ```powershell
  python evidence/count.py --data-dir ../K5-L3-Day15-AI-Product-Hackathon/data/preclass
  ```

## 2. Đọc trước, đếm sau

Đã đọc 35 dòng đầu của `events.csv`, `answers.csv`, `chat.csv`, `learners.csv` cùng từ điển cột (`column_dictionary.csv`, `event_types.csv`). Các *kiểu* hành vi thấy được:
- Nhiều lượt học viên mở video (`video_opened`), có `open_count >= 2` (quay lại mở lại video) và chuyển tab ẩn màn hình (`app_visibility_changed`, `visible: false`).
- Xuất hiện nhiều chuỗi `video_seeked` tua lùi liên tiếp vài chục giây (dấu hiệu tìm lại đoạn vừa trôi qua) hoặc `quiz_item_dismissed` với `skipped_stop = True`.
- Ở `answers.csv`, các câu trắc nghiệm/kiểm tra (`pre_post_post`, `thuc_hanh`) ở `lan_thu = 1` có trường `was_correct = False`, cho thấy học viên vẫn sai dù đã xem bài trước đó.
- Ở `chat.csv`, phần lớn lượt nhắn là hỏi trực tiếp ngay dưới video/slide (`video_question`), thậm chí có câu hỏi rất ngắn (`do_dai_cau_hoi = 2`).

## 3. Kết quả

| Đếm gì | x / N | % | Ghi chú |
|---|---:|---:|---|
| Học viên có hoạt động / tổng tài khoản | 436 / 721 | 60.5% | `events.csv` / `learners.csv` |
| Học viên từng mở video / học viên hoạt động | 431 / 436 | 98.9% | Tổng `7.254` lượt `video_opened` |
| Học viên từng xem hết ≥ 1 video / học viên mở video | 171 / 431 | 39.7% | Tổng `1.867` lượt `video_ended` |
| Lượt tua lùi (`to < from`) / tổng lượt tua `video_seeked` | 2602 / 4322 | 60.2% | Tua tiến: `1641/4322 (38.0%)` |
| Học viên từng tua lùi / học viên mở video | 177 / 431 | 41.1% | — |
| Học viên mở lại cùng video ≥ 2 lần / học viên mở video | 213 / 431 | 49.4% | `1055/7254 (14.5%)` lượt mở video |
| Lượt đóng bỏ qua quiz giữa video (`skipped_stop=True`) / `quiz_item_dismissed` | 21 / 2099 | 1.0% | `17/189 (9.0%)` học viên từng mở quiz |
| Sai lần đầu bài kiểm tra sau học (`pre_post_post`, `lan_thu=1`) | 399 / 1968 | 20.3% | **`69/77 (89.6%)`** học viên làm phần này từng sai ít nhất 1 câu |
| Sai lần đầu thực hành (`thuc_hanh`, `lan_thu=1`) | 23 / 503 | 4.6% | `12/113 (10.6%)` học viên từng sai ở lần đầu |
| Lượt hỏi AI dưới video (`video_question`) / tổng `chat.csv` | 1108 / 1260 | 87.9% | `145/431 (33.6%)` học viên mở video từng hỏi |

## 4. ≥5 ví dụ cụ thể (mã dòng / mã đã ẩn danh, không đoán ai là ai)

1. `events.csv:73` · `L0006` · video `d01-r1-v01` · tua lùi `88.9s -> 40.8s` (`2026-11-05T10:55:51Z`)
2. `events.csv:171` · `L0503` · video `d01-r1-v01` · tua lùi `129.9s -> 118.8s` (sau đó `events.csv:172` tua lùi tiếp `118.8s -> 101.1s`)
3. `events.csv:195` · `L0503` · câu hỏi `day01-ai-llm-foundation:m01:s007` · đóng bỏ qua câu hỏi giữa video (`skipped_stop=True`)
4. `events.csv:16428` · `L0379` · câu hỏi `day01-ai-llm-foundation:m01:s007` · đóng bỏ qua câu hỏi giữa video (`skipped_stop=True`)
5. `answers.csv:3` · `A00611` · `L0213` · `nguon=pre_post_post` · `ref=d01-on-chatbot-la-ung-dung` · `lan_thu=1` · `was_correct=False`
6. `answers.csv:61` · `A00340` · `L0057` · `nguon=thuc_hanh` · `ref=lab:d02-lab-chon-muc-giai-phap:chon-muc` · `lan_thu=1` · `was_correct=False`

## 5. Giới hạn của data

Data cho biết người ta **làm gì**, không cho biết **vì sao**. Thiếu gì, lệch về phía nào:
- Không có nội dung câu chữ mà học viên đã viết/hỏi (chỉ có độ dài ký tự `do_dai_cau_hoi`), nên không biết học viên kẹt chính xác ở ý nào khi tua lùi.
- Câu hỏi giữa video (`video_quiz`) mới ghi `7` dòng trong `answers.csv` (trong khi `events.csv` có `2.153` lượt `quiz_item_opened`), nên chưa đo đủ tỉ lệ đúng/sai ngay trong video từ `answers.csv`; các event `checkpoint_presented` / `checkpoint_skipped` hiện có `0` dòng (tính năng checkpoint chưa được bật trong đợt log này).
- Tốc độ xem `last_rate > 1` ghi nhận `0/22.751 (0.0%)` và `crossed_stop = True` là `0/4.322 (0.0%)`.

→ Kiểm lại bằng phỏng vấn / khảo sát nào: Phỏng vấn **≥ 3 học viên L3A ngoài nhóm** (`evidence/interviews/P1.md`–`P3.md`) để hỏi lý do thật đằng sau hành vi tua lùi nhiều (`60.2%`) và tỉ lệ học viên sai lần đầu cao (`89.6%` ở `pre_post_post`).
