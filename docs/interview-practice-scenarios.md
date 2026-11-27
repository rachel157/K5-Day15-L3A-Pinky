# Bộ 10 kịch bản hành vi học viên & Ánh xạ vào bộ câu thử (Chu Mai Hồng — BA)

> **CẢNH BÁO MINH BẠCH (theo `AGENTS.md` và `03-rubric.md` R1):**  
> 10 câu trả lời dưới đây là **kịch bản giả lập (synthetic personas) để tập dượt phỏng vấn Mom Test và thiết kế lưới phủ độ khó cho `eval/benchmark.csv`**.  
> - **TUYỆT ĐỐI KHÔNG** chép 10 kịch bản này thành `evidence/interviews/P1.md`… hay trích dẫn như người thật trong `evidence/summary.md`.  
> - Trong `eval/benchmark.csv`, các câu thử sinh từ 10 kịch bản này đã được gắn nhãn nguồn trung thực là `tu_viet` (hoặc `data_that` khi gắn trực tiếp với mã dòng log có thật trong `data/preclass`).

---

## 1. Bảng ánh xạ 10 kịch bản thực tế sang `eval/benchmark.csv`

| # | Kiểu hành vi học viên trên `preclass-online.com` | Chiều hướng so với giả thuyết | Câu trả lời mô phỏng (theo 3 câu hỏi Mom Test) | Mã câu thử trong `eval/benchmark.csv` |
|---|---|---|---|---|
| **1** | Đi làm về muộn, xem gấp buổi tối, bỏ qua quiz giữa video → sang mini lab mới phát hiện quên ý chính | **Khớp giả thuyết** | *"Tối đi làm về muộn mới mở bài xem tốc độ nhanh cho kịp sáng hôm sau. Lúc câu hỏi giữa video bật lên mình bấm đóng cho qua, tới lúc mở mini lab mới quên mất điều kiện áp dụng, phải kéo thanh tua mò lại 4–5 chỗ mất gần 10 phút."* | `C07`, `C14` |
| **2** | Học kỹ, dừng lại ghi chú đầy đủ từng mốc ý chính → qua lab trơn tru | **Ngược giả thuyết** *(không gặp pain, không muốn bị làm phiền)* | *"Mình xem tốc độ 1x, mở Notion ghi lại ý chính kèm mốc phút, làm hết câu hỏi giữa video nên qua mini lab làm một mạch, không phải quay lại tìm video."* | `C01`, `C13` |
| **3** | Vừa mở video vừa chuyển tab làm việc khác / nhắn tin → đứt mạch giữa chừng | **Khớp giả thuyết** *(khớp log `app_visibility_changed` trong `events.csv`)* | *"Mình hay vừa mở video vừa trả lời tin nhắn công ty ở tab khác. Lúc quay lại gặp câu hỏi thì ngớ người không biết bài vừa nói gì và bị hụt từ phút thứ mấy, mò lại mất 5–7 phút."* | `C17` |
| **4** | "Ảo giác hiểu bài" — xem thấy rất xuôi nhưng làm bài kiểm tra mới biết hiểu nhầm hai khái niệm gần nhau | **Khớp giả thuyết** *(khớp `89.6%` học viên từng sai lần đầu ở `pre_post_post`)* | *"Xem video thấy thầy giảng dễ hiểu nên xem thẳng một lèo. Đến lúc làm câu hỏi ôn tập cuối bài mới biết bị nhầm hai khái niệm na ná nhau, mò lại đoạn phân biệt mất 8 phút."* | `C02`, `C08`, `C15` |
| **5** | Học ngược quy trình: mở mini lab đọc đề trước, bí chỗ nào mới bật video tra ngược lại | **Ngược giả thuyết** *(cần tra cứu nhanh mã đoạn, ghét bị khóa/chặn)* | *"Mình ít khi xem video từ đầu đến cuối mà mở mini lab trước, vướng bước nào mới bật video lướt tìm đúng đoạn đó. Nếu bị câu hỏi chặn cứng giữa chừng sẽ rất khó chịu."* | `C18` |
| **6** | Gặp chỗ khó là bôi đen hỏi Trợ giảng AI dưới slide / ChatGPT nhưng vẫn cần tìm lại ví dụ trong video gốc | **Khớp một phần** *(khớp `87.9%` chat là `video_question`)* | *"Khi thấy lùng bùng mình hỏi trợ giảng AI ngay dưới bài cho nhanh, nhưng đôi khi câu trả lời hơi chung chung và mình vẫn không biết đoạn video gốc thầy lấy ví dụ nằm ở chỗ nào."* | `C19` |
| **7** | Xem lướt cho đủ thanh tiến độ, gặp câu hỏi thì gõ 1–2 chữ hoặc đoán đại | **Biên độ khó (Lớp 2)** *(khớp `chat.csv` có câu dài 2 ký tự)* | *"Mấy hôm bận mình mở video cho chạy hết thanh tiến độ, câu hỏi bật lên thì gõ đại hoặc đoán bừa cho qua, vào lớp hoặc làm lab mới bị hổng."* | `C06`, `C10`, `C20` |
| **8** | Học trên điện thoại khi di chuyển → rất ngại thao tác kéo thanh tua trên màn hình nhỏ | **Khớp giả thuyết** *(khớp `device_class: phone` trong `events.csv`)* | *"Xem trên điện thoại lúc đi xe buýt, màn hình nhỏ nên kéo thanh tua nhẹ tay là nhảy mất 20–30 giây. Thành ra rất cần được trỏ thẳng tới đúng đoạn thay vì tự kéo tua."* | `C16` |
| **9** | Quá tải tương tác khi vừa có bạn học AI (`maic`) vừa có câu hỏi → muốn bỏ qua hoặc đòi hệ thống tự đánh dấu hoàn thành | **Ngược giả thuyết / Lớp 3** | *"Đang nghe giảng mà nhiều lời xen vào quá làm mình bị loạn nhịp, chỉ muốn tắt bớt hoặc cho qua luôn để xem tiếp theo tốc độ của mình."* | `C22` |
| **10** | Học bù dồn 2–3 bài liên tiếp cuối tuần → lẫn lộn khái niệm giữa bài trước và bài sau | **Khớp giả thuyết (Lớp 4)** | *"Cuối tuần học bù liền 3 video từ Day01 sang Day02, tới lúc làm bài tập tổng hợp thì lẫn khái niệm của bài 1 với bài 2, không nhớ nó nằm ở đoạn nào."* | `C21` |

---

## 2. Độ phủ của bộ 22 câu thử trong `eval/benchmark.csv`

- **Tổng số câu:** `22` câu (đạt chuẩn cả **CP2 ≥ 10 câu** và **CP3 20–30 câu**).
- **Phân bố theo loại (`type`):**
  - `thuong`: **8 câu** (`C01`–`C04`, `C13`–`C16`)
  - `kho`: **11 câu** (`C05`–`C10`, `C17`–`C21` — phủ đủ 4 lớp chỗ khó trong `spec.md` §5)
  - `tu_choi`: **3 câu** (`C11`, `C12`, `C22` — gồm các kịch bản tấn công prompt injection, đòi chấm 10/10, đòi giải hộ mini lab, đòi sửa `item_completed=True`)
- **Phân bố theo nguồn (`source`):**
  - `data_that`: **8/22 câu (`36.4% >= 1/3`)** — trỏ trực tiếp tới các bản ghi có thật trong `data/preclass` (`A00611`, `A00288`, `A00340`, `C01056`, `L0503`, `A01988`, `A00550`, `L0494`/`A02608`).
  - `tu_viet`: **14/22 câu (`63.6%`)** — bao phủ trọn vẹn 10 kịch bản hành vi thực tế và các trường hợp biên/tấn công.
