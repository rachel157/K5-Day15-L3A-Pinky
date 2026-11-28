# Tóm tắt mô phỏng simulate-2@20261128-071851

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dung_it | 20 | 1 | 480 | 61 | 0.7 | 2.2 |
| dung_vua | 19 | 2 | 1143 | 151 | 1.7 | 5.1 |
| dung_nhieu | 11 | 3 | 1620 | 215 | 2.4 | 7.4 |

Tỉ lệ đạt dùng để tính: 20/22 (91%) — lượt run-2@20261128-071526

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv (--rate-from).

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (177 người) | Chi phí / tháng — cơ sở (213 người) | Chi phí / tháng — cao (431 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-5.4-mini-2026-03-17 (vào 0.75 · ra 4.5 $/1M) | $0.0013 | $0.0014 | $0.00080 | $1.37 | $1.65 | $3.35 | $0.0078 |
| gemini-3.1-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.00044 | $0.00048 | $0.00027 | $0.4582 | $0.5514 | $1.12 | $0.0026 |
| gemini-3.5-flash-lite (vào 0.3 · ra 2.5 $/1M) | $0.00062 | $0.00068 | $0.00037 | $0.6444 | $0.7755 | $1.57 | $0.0036 |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.8) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gpt-5.4-mini-2026-03-17. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
