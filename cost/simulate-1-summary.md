# Tóm tắt mô phỏng simulate-1@20261127-190653

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

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
