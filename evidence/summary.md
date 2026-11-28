# Tổng hợp bằng chứng pain

> Điền ở guide bước 1.2, xong trước **CP3 10:00 Thứ Bảy 28/11**. Chấm ở rubric R1.
> Ba nguồn ngang nhau — tối thiểu **≥1 nguồn đạt ngưỡng**. Mạnh nhất: đào data ra insight → hỏi người dùng để kiểm lại (hoặc ngược lại).

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | File |
|---|---|---|
| Đào data (x/N, %, cách đếm chạy lại được, ≥5 ví dụ) | ☑ **Đạt ngưỡng chính** | `evidence/data-mining.md` (+ `evidence/count.py`) |
| Phỏng vấn (≥3 người ngoài nhóm, đúng người dùng) | ☑ **Đạt ngưỡng đối chiếu (3 học viên `P1`–`P3`)** | `evidence/interviews/P1.md`, `P2.md`, `P3.md` |
| Khảo sát (≥20 người ngoài nhóm, đúng người dùng) | ☐ *(Bổ trợ: 11 phản hồi ẩn danh từ học viên L3 ngoài nhóm)* | `evidence/survey/questions.md`, `evidence/survey/results.csv` |

## 2. Số chính

- **Đào data (`data/preclass`, Day01–Day13, `431` học viên xem video):**
  - `2.602/4.322 (60.2%)` lượt tua video là tua lùi (`177/431 = 41.1%` học viên mở video từng tua lùi).
  - `213/431 (49.4%)` học viên phải mở lại cùng một video ≥ 2 lần (`1.055/7.254 = 14.5%` lượt mở).
  - Tỉ lệ đóng bỏ qua câu hỏi giữa video (`skipped_stop = True`) chỉ `21/2.099 (1.0%)` lượt, nhưng khi làm bài kiểm tra sau học (`pre_post_post`) có tới `399/1.968 (20.3%)` lượt trả lời sai ngay lần đầu (`69/77 = 89.6%` học viên làm phần này từng sai ít nhất 1 câu).
  - `1.108/1.260 (87.9%)` lượt chat AI là hỏi trực tiếp dưới video/slide (`video_question`).
- **Phỏng vấn học viên L3A ngoài nhóm (`P1`–`P3` tại `evidence/interviews/P1.md`..`P3.md`):**
  - **3/3 học viên** xác nhận từng xem xong video thấy hiểu ("nghe giảng xuôi tai"), nhưng khi bước vào làm câu hỏi cuối bài hoặc bài thực hành mới phát hiện mình nhớ nhầm giữa các khái niệm gần nhau hoặc quên ý chính.
  - **3/3 học viên** chỉ giải quyết được **một phần** khi quay lại video (tìm mãi trong video không thấy đúng chỗ nên phải tra thêm ChatGPT/Claude hoặc hỏi Trợ giảng AI dưới video).
  - Số lần phải quay lại video tua tìm đoạn trong 1 tháng qua: `P1` = **6 lần**, `P2` = **6 lần**, `P3` = **3 lần** (trung bình **5 lần/tháng**, trung vị **6 lần/tháng**).
  - Thời gian mất ở lần gần nhất: `P1` = **3–5 phút**, `P2` = **10–15 phút**, `P3` = **5–10 phút**.
- **Phiếu khảo sát Mom Test mở rộng (`11` học viên L3 ngoài nhóm — `10` L3A, `1` L3 lớp khác tại `evidence/survey/results.csv`):**
  - **11/11 người** đều gặp tình trạng xem video xong tưởng đã hiểu nhưng tới lúc làm câu hỏi / mini lab / nghe Lab Coach hỏi mới nhận ra mình hổng hoặc nhầm khái niệm (`4/11` vừa gặp ở Day13–Day14, `4/11` gặp trong tuần này Day10–Day12, `3/11` gặp ở tuần trước Day05–Day09).
  - **9/11 người** phải mở lại video và tự kéo thanh tua lùi nhiều lần để mò đoạn thầy giảng; **7/11 người** tìm mãi trong video không thấy đúng chỗ nên chỉ giải quyết được một phần và phải tra nguồn khác (`7/11` mở ChatGPT/Claude bên ngoài, `5/11` bấm hỏi khung chat Trợ giảng AI dưới video).
  - Trong 9 người nhập con số cụ thể ở câu số lần/tháng (`1, 2, 2.5, 3, 4, 6, 6, 6, 7`, còn 2 người ghi *"Nhiều lần, rất nhiều"* và *"Tua lại slide nhiều lần"*), trung bình là **4.2 lần/tháng** (các học viên gặp thường xuyên rơi đúng vào mốc **6–7 lần/tháng**).
  - Thời gian mất mỗi lần tìm lại đoạn: `3/11` người mất **1–2 phút**, `3/11` người mất **3–5 phút**, `3/11` người mất **5–10 phút**, `2/11` người mất **10–15 phút** (trung vị rơi vào khoảng **4–5 phút/lần**).

Phỏng vấn nhiều vai thì đếm theo từng vai, không cộng chung.

| | Vai | Gặp pain? | Số lần / 1 tháng qua | Lần gần nhất mất | Đang xoay xở bằng |
|---|---|---|---|---|---|
| **P1** | Học viên L3A (ngoài nhóm) | **Có** (nhầm điều kiện áp dụng giữa 2 phương pháp khi học Prompt Engineering / RAG) | `6` lần | `3 - 5` phút | Mở lại video tự kéo thanh tua lùi nhiều lần + hỏi khung chat Trợ giảng AI dưới video + mở ChatGPT/Claude (chỉ xong một phần trong video) |
| **P2** | Học viên L3A (ngoài nhóm) | **Có** (hiểu khi xem video nhưng nhầm giữa `for` và `while` khi làm bài thực hành) | `6` lần | `10 - 15` phút | Xem lại ghi chú cá nhân (Notion/sổ tay) + tự tua đi tua lại video vì làm sai câu hỏi trên web chưa có giải thích cụ thể gắn với đoạn bài |
| **P3** | Học viên L3A (ngoài nhóm) | **Có** (xem video Day13–14 thấy rất hiểu nhưng làm bài bị quên, phải lần lại từng bước) | `3` lần | `5 - 10` phút | Mở lại video kéo thanh tua lùi qua nhiều đoạn + bấm hỏi Trợ giảng AI dưới video + ChatGPT/Claude (sợ bỏ sót nội dung khi tua) |

## 3. ≥5 trích dẫn hoặc ví dụ nguyên văn (có nguồn, bỏ tên)

1. **`P1` (`evidence/interviews/P1.md`, `evidence/survey/results.csv` dòng 4):** *"Khi học phần Prompt Engineering / RAG tuần trước, lúc nghe giảng mình tưởng đã nắm rõ cách chia chunk và thiết kế luồng, nhưng lúc làm câu hỏi cuối bài mới nhận ra mình nhớ nhầm điều kiện áp dụng giữa hai phương pháp."*
2. **`P1` (`evidence/interviews/P1.md`, `evidence/survey/results.csv` dòng 4):** *"Video bài giảng khá dài nhưng chưa chia mốc thời gian (timestamps) theo từng mục nhỏ hoặc chưa có khung tìm kiếm theo nội dung lời thoại/slide. Mỗi lần quên một chi tiết nhỏ ở phần thực hành, mình phải kéo thanh tua thủ công và nghe lại nhiều đoạn không liên quan mới tìm đúng chỗ thầy giải thích, rất mất thời gian."*
3. **`P2` (`evidence/interviews/P2.md`, `evidence/survey/results.csv` dòng 6):** *"Việc bất tiện nhất là phải tự tua đi tua lại video để tìm đúng đoạn kiến thức mình chưa hiểu, khá mất thời gian vì đôi khi không nhớ chính xác nội dung nằm ở phút nào. Ngoài ra, khi làm câu hỏi kiểm tra trên web, nếu trả lời sai thì chưa phải lúc nào cũng có phần giải thích cụ thể nên mình phải quay lại video để xem và hiểu lại kiến thức."*
4. **`P3` (`evidence/interviews/P3.md`, `evidence/survey/results.csv` dòng 8):** *"xem video rất hiểu nhưng hay bị quên kiến thức xem lại mất thời gian phải lần lại từng bước... khi tìm lại lý thuyết video mất thời gian tua để đến đoạn cần mà nhiều đoạn nên là vẫn có thể bị bỏ sót nội dung"*
5. **Học viên L3A ẩn danh #8 (`evidence/survey/results.csv` dòng 9):** *"Không biết kiến thức đó ở đoạn nào để tua, tua về quá mất kiến thức xong mất dấu chỗ đang học."*
6. **Log hành vi & kiểm tra thật (`data/preclass` — `evidence/data-mining.md`):**
   - `events.csv:73` — `L0006` tua lùi video `d01-r1-v01` từ `88.9s -> 40.8s`; `events.csv:171-172` — `L0503` tua lùi 2 lần liên tiếp (`129.9s -> 118.8s -> 101.1s`).
   - `answers.csv:3` — `A00611` (`L0213`) trả lời sai ngay lần đầu câu kiểm tra `d01-on-chatbot-la-ung-dung` (`pre_post_post`, `lan_thu=1`).

## 4. Các nguồn có khớp nhau không

- **Khớp chặt chẽ cả về hiện tượng lẫn con số định lượng:**
  1. **Về hiện tượng ("Ảo giác hiểu bài"):** Log `data/preclass` cho thấy học viên rất ít bỏ qua quiz giữa video (`1.0%` lượt) nhưng lại sai lần đầu tới `20.3%` lượt (`89.6%` học viên) ở bài kiểm tra sau học (`pre_post_post`). Lời kể của `P1`, `P2`, `P3` và 11 học viên khảo sát giải thích chính xác nguyên nhân: *"lúc nghe giảng xuôi, lúc làm không áp dụng được"*, *"lúc xem video rất ổn nhưng lúc làm bài thì lại thấy mình chưa hiểu sâu"* và bị nhầm điều kiện áp dụng giữa hai khái niệm gần nhau.
  2. **Về hành vi tua mò & mất dấu:** Log ghi nhận `60.2%` lượt tua là tua lùi và `49.4%` học viên phải mở lại cùng video ≥ 2 lần. Phỏng vấn & khảo sát xác nhận `9/11` học viên phải tự kéo thanh tua lùi nhiều lần vì không nhớ khái niệm nằm ở phút:giây nào, dẫn đến `7/11` người tìm mãi trong video không thấy đúng chỗ và bị *"mất dấu chỗ đang học"*.
  3. **Về tần suất & thời gian mất (kiểm chứng giả định bảng Impact `spec.md` §2):** Con số ước tính từ log ở CP2 (`~6` lần/tháng × `~4` phút/lần) khớp sát với số thực tế do học viên báo cáo (`P1`, `P2` đều gặp `6` lần/tháng; trung vị thời gian mất của 11 học viên khảo sát là nhóm `3 - 5` phút và `5 - 10` phút).

## 5. Kết luận

- **Giả thuyết ĐÚNG và được làm sắc nét hơn nhờ kết hợp Đào data + Phỏng vấn/Khảo sát:** Học viên lớp L3 không cố tình bỏ qua việc học mà gặp **"ảo giác hiểu bài"** khi xem video một chiều; khi phát hiện lỗ hổng ở câu hỏi kiểm tra hoặc bài thực hành, họ mất trung bình 4–6 phút mỗi lần (3–6 lần/tháng) để tự kéo thanh tua mò lại đoạn giảng nhưng đa số (`7/11` người) không tìm lại được đúng chỗ ngay trong video. Giải pháp **Checkpoint Tutor** (kiểm tra hiểu ngắn tại điểm dừng, chỉ rõ điểm nhầm lẫn và gắn nút nhảy đúng đoạn cần xem lại mà không khóa video) đánh trúng trực tiếp vào chỗ đau này.

## Lịch hẹn (dùng cho CP2 — chỉ ghi vai và giờ, không tên)

| Vai | Giờ hẹn | Đã xong? |
|---|---|---|
| Học viên L3A (ngoài nhóm) — P1 | 18:30–19:05 Thứ Sáu 27/11 (`evidence/interviews/P1.md`) | ☑ |
| Học viên L3A (ngoài nhóm) — P2 | 18:30–19:15 Thứ Sáu 27/11 (`evidence/interviews/P2.md`) | ☑ |
| Học viên L3A (ngoài nhóm) — P3 | 18:30–19:30 Thứ Sáu 27/11 (`evidence/interviews/P3.md`) | ☑ |
