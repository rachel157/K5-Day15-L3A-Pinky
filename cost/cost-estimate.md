# Chi phí khi dùng thật

## 1. Đầu vào

- Cấu hình: `cost/personas.yaml`, 50 phiên, seed 42; 3 persona, tổng share = 1.
- `dung_it`: 50%, 2 phiên/người/tháng, 1 lượt/phiên; `dung_vua`: 30%, 6 phiên/tháng, 2 lượt/phiên; `dung_nhieu`: 20%, 10 phiên/tháng, 3 lượt/phiên. Tỷ trọng và số lượt là **tự ước tính**; tần suất bám `spec.md` §2, chưa có xác nhận phỏng vấn.
- Ba kịch bản: thấp 177 người từng tua lùi, cơ sở 213 người mở lại video, cao 431 người từng mở video. Số từ `evidence/data-mining.md`/`spec.md` §1–2; lựa chọn ba nhóm làm quy mô triển khai là **tự ước tính**, không cộng các nhóm chồng lấn.
- Token thực đo trên **gpt-5.4-mini-2026-03-17**. Tính giá OpenAI và so sánh giả định giá Gemini; chưa đo chất lượng hoặc token thực tế trên Gemini.
- Giá Standard text, USD/1 triệu token vào/ra: OpenAI 0.75/4.50 ([nguồn](https://developers.openai.com/api/docs/models/gpt-5.4-mini.md)); Gemini 3.1 Flash-Lite 0.25/1.50 và Gemini 3.5 Flash-Lite 0.30/2.50 ([nguồn](https://aistudio.google.com/docs/pricing)). Xem 27/11/2026.
- Toàn bộ input tính theo giá không cache (ước tính bảo thủ); khung không tách cached input. Chưa tính hosting, lưu trữ, nhân công hay thuế; không quy đổi VND khi chưa có tỷ giá có nguồn.
- Chưa có tỷ lệ đạt chính thức: `eval/run-1.csv` đã chạy đủ 22 câu nhưng cột pass chờ Vũ/Hồng duyệt. `score` báo 0/22 câu đã chấm, không phải 0/22 câu đạt.

## 2. Kết quả mô phỏng

Lượt: `cost/simulate-1.csv` · run ID `simulate-1@20261127-190653` · 50 phiên · seed 42. Bảng dưới chép nguyên từ `cost/simulate-1-summary.md`, không sửa file summary/CSV/trace.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dung_it | 20 | 1 | 222 | 51 | 0.8 | 2.4 |
| dung_vua | 19 | 2 | 471 | 109 | 1.7 | 5.1 |
| dung_nhieu | 11 | 3 | 742 | 180 | 2.6 | 7.9 |

Tỉ lệ đạt dùng để tính: **chưa có** lượt eval nào chấm xong (`python run.py score eval/run-N.csv`) → chưa tính được chi phí / task thành công

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (177 người) | Chi phí / tháng — cơ sở (213 người) | Chi phí / tháng — cao (431 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-5.4-mini-2026-03-17 (vào 0.75 · ra 4.5 $/1M) | $0.00078 | — | — | $0.8227 | $0.9901 | $2.00 | $0.0046 |
| gemini-3.1-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.00026 | — | — | $0.2742 | $0.3300 | $0.6678 | $0.0015 |
| gemini-3.5-flash-lite (vào 0.3 · ra 2.5 $/1M) | $0.00038 | — | — | $0.4043 | $0.4866 | $0.9846 | $0.0023 |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.8) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gpt-5.4-mini-2026-03-17. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.

## 3. So với impact

- `spec.md` §2 ước tính 6 lần/người/tháng × 4 phút = **24 phút/người/tháng**; chưa phải hiệu quả học tập đã đo.
- OpenAI ở kịch bản cơ sở: **$0.0046/người/tháng**, khoảng **$0.9901/tháng cho 213 người** theo hành vi giả định.
- Chi phí model thấp nhưng **chưa đủ căn cứ kết luận đáng triển khai**: lượt 1 còn chọn sai đoạn và xác nhận câu trả lời sai; xem `eval/report.md`.
- Một số nhánh xử lý bằng luật không gọi model nên token bằng 0; số liệu phản ánh workflow hiện tại, không phải cam kết chi phí cho Agent sau cải tiến.

## 4. Còn phải hoàn tất

- Vũ/Hồng duyệt chấm lượt 1 và đối chiếu độc lập 5 câu; Tùng cải tiến nhóm lỗi; Vũ chạy lượt 2.
- Sau khi lượt 2 được chấm, chạy `python run.py score eval/run-2.csv`, rồi `python run.py simulate --rate-from eval/run-2.csv` (dùng tên lượt thực tế).
- Lượt mô phỏng hiện tại là đo chi phí trước cải tiến, chưa phải báo cáo cuối sau lượt 2. Giữ nguyên các lần chạy đã sinh.
