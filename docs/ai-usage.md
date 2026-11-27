# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Môi trường và kết nối model | Codex | Viết adapter Gemini/OpenAI/Anthropic trong `codebase/ai.py`, kiểm tra kết nối | Kiểm tra qua app với AI thật (`tokens_in`/`tokens_out` > 0 từ `usage`, bật `store: False`), giữ chế độ `fake` mặc định | Phạm Nguyên Vũ |
| Vận hành eval và mô phỏng | Codex, Antigravity | Chạy bộ 22 câu bằng API thật và mô phỏng 50 phiên; viết `eval/check_code_metrics.py` kiểm tự động 2 metric `code`; lập bảng nháp rà 22 câu trong `eval/report.md`; cập nhật giá và giả định chi phí | Bản chấm nháp 22 câu chờ Vũ/Hồng duyệt; cột `pass` trong `eval/run-1.csv` giữ trống cho đến khi người chấm xác nhận | Phạm Nguyên Vũ |
| Code bản chạy thử & Giao diện Demo | Antigravity, Codex | Hỗ trợ viết `codebase/agent.py`, `codebase/tools.py`, chuẩn hóa 15 đoạn trong `data/lesson.json` và dựng UI trình phát video + khung chat Trợ giảng AI (`demo/index.html`, `demo/demo_server.py`) | Sửa logic chống chấm sai câu phủ định (`C03`), sửa trọng số alias retrieval (`C01`, `C15`, `C16`, `C19`, `C20`), ẩn mã kỹ thuật khỏi UI học viên (đưa vào nút `?`), thêm rào chắn 0-token chống Prompt Injection & dùng chùa token | Nguyễn Hoàng Tùng |
| Prompt / thiết kế lời gọi mô hình | Antigravity, Codex | Tối ưu `SYSTEM` prompt và `CHAT_SYSTEM` prompt với delimiter `<<<...>>>` và giới hạn độ dài phản hồi | Kiểm tra độ dài output `<= 165` từ để đạt metric `do_gon_tai_diem_dung_va_hieu_qua_thuc_thi` và không lộ mã nội bộ ra UI | Nguyễn Hoàng Tùng |
| Đào data (viết script đếm, gợi ý nhãn) | | | Kiểm tay __ dòng, khớp __ | |
| Rà câu hỏi phỏng vấn / khảo sát | | Chỉ rà câu dẫn dắt | | |
| Viết câu thử (benchmark) | | | Mỗi câu thử có `source`; câu thử AI viết được ghi rõ | |
| Sinh data `synthetic` (nếu có) | | | Seed __ · kiểm tay __ dòng | |
| Chấm cột `pass` bằng LLM (nếu có) | | | Kiểm tra thủ công __ câu thử, khớp __/__ | |
| Slide, văn bản | | | | |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
