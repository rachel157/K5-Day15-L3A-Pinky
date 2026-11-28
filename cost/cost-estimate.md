# Chi phí khi dùng thật

## 1. Đầu vào

- Cấu hình: `cost/personas.yaml`, 50 phiên, seed 42; 3 persona, tổng share = 1.
- `dung_it`: 50%, 2 phiên/người/tháng, 1 lượt/phiên; `dung_vua`: 30%, 6 phiên/tháng, 2 lượt/phiên; `dung_nhieu`: 20%, 10 phiên/tháng, 3 lượt/phiên. Tỷ trọng và số lượt là **tự ước tính**; tần suất bám `spec.md` §2, chưa có xác nhận phỏng vấn.
- Ba kịch bản: thấp 177 người từng tua lùi, cơ sở 213 người mở lại video, cao 431 người từng mở video. Số từ `evidence/data-mining.md`/`spec.md` §1–2; lựa chọn ba nhóm làm quy mô triển khai là **tự ước tính**, không cộng các nhóm chồng lấn.
- Token thực đo trên **gpt-5.4-mini-2026-03-17**. Tính giá OpenAI và so sánh giả định giá Gemini; chưa đo chất lượng hoặc token thực tế trên Gemini.
- Giá Standard text, USD/1 triệu token vào/ra: OpenAI 0.75/4.50 ([nguồn](https://developers.openai.com/api/docs/models/gpt-5.4-mini.md)); Gemini 3.1 Flash-Lite 0.25/1.50 và Gemini 3.5 Flash-Lite 0.30/2.50 ([nguồn](https://aistudio.google.com/docs/pricing)). Xem 27/11/2026.
- Toàn bộ input tính theo giá không cache (ước tính bảo thủ); khung không tách cached input. Chưa tính hosting, lưu trữ, nhân công hay thuế; không quy đổi VND khi chưa có tỷ giá có nguồn.
- Tỷ lệ đạt dùng để tính chi phí lấy từ [eval lượt 2](../eval/run-2.csv), đã chốt sau khi Hồng xác nhận cột `pass`.

## 2. Kết quả mô phỏng

Lượt đo sau cải tiến: [simulate-2.csv](simulate-2.csv) · `simulate-2@20261128-071851` · 50 phiên · seed 42.
Số liệu lấy từ [tóm tắt tự sinh](simulate-2-summary.md). Lưu [lượt đo trước cải tiến](simulate-1-summary.md) để đối chiếu.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dung_it | 20 | 1 | 480 | 61 | 0.7 | 2.2 |
| dung_vua | 19 | 2 | 1143 | 151 | 1.7 | 5.1 |
| dung_nhieu | 11 | 3 | 1620 | 215 | 2.4 | 7.4 |

Tỉ lệ đạt dùng để tính: 20/22 (90,9%) — lượt run-2@20261128-071526

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv (--rate-from).

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (177 người) | Chi phí / tháng — cơ sở (213 người) | Chi phí / tháng — cao (431 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-5.4-mini-2026-03-17 (vào 0.75 · ra 4.5 $/1M) | $0.0013 | $0.0014 | $0.00080 | $1.37 | $1.65 | $3.35 | $0.0078 |
| gemini-3.1-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.00044 | $0.00048 | $0.00027 | $0.4582 | $0.5514 | $1.12 | $0.0026 |
| gemini-3.5-flash-lite (vào 0.3 · ra 2.5 $/1M) | $0.00062 | $0.00068 | $0.00037 | $0.6444 | $0.7755 | $1.57 | $0.0036 |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.8) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gpt-5.4-mini-2026-03-17. Hai dòng Gemini là ước tính theo bảng giá Gemini, dùng số token đo trên GPT. Số token thực tế khi chạy bằng Gemini có thể khác.
- Phiên lỗi (không tính vào trung bình): 0/50.

## 3. So với impact

- `spec.md` §2 ước tính 6 lần/người/tháng × 4 phút = **24 phút/người/tháng**. Đây là thời gian vướng ước tính, hiệu quả tiết kiệm thời gian chưa được đo.
- OpenAI ở kịch bản cơ sở: **$0.0078/người/tháng**, khoảng **$1.65/tháng cho 213 người** theo tần suất giả định.
- Một số nhánh xử lý bằng luật dùng 0 token. Số liệu phản ánh luồng hiện tại và quy mô giả định.
