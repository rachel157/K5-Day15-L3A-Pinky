# Data card — dữ liệu bản chạy thử dùng

> Điền ở guide bước 2.4 (bản đầu ở CP2, đủ ở CP3). Ôn lại: ngày 6 · lab ngày 6. Chấm ở rubric R4.
> Một trang. Mỗi dataset một mục. Dữ liệu chạy thử (bài mẫu, thông báo mẫu, đoạn transcript…) để trong thư mục `data/` này.
> Không commit nguyên tài liệu khoá, dữ liệu cá nhân thật hay nguyên file data BTC cấp — chỉ đoạn trích ngắn, bản viết lại, hoặc số đã tổng hợp.

## Dataset 1 · Bộ đoạn bài giảng & điểm dừng Checkpoint mẫu (Day01, Day02)

| | |
|---|---|
| Dùng để làm gì | Nguồn tra cứu cho công cụ trong `codebase/tools.py` · Ngữ cảnh bài học và mã đoạn chuẩn cho 22 câu thử trong `eval/benchmark.csv` |
| Từ đâu | Tổng hợp và viết lại ngắn gọn theo cấu trúc bài học (`program-day01:ai-llm-foundation`, `program-day02:ai-problem-definition`) và danh mục mã ý kiến thức (`kc_code`) có thật trong `data/preclass` (`chatbot_is_app_around_model`, `model_tier_selection`, `temperature_stability_not_truth`, `token_generation_loop_count`, `stop_reason_output_limit`, `cutoff_and_hallucination`, `context_keep_table_clean`, `memory_lives_in_the_app`, `select_rule_workflow_agent_level`, `make_go_not_yet_no_go_decision`). Không sao chép nguyên văn tài liệu khoá. |
| Xử lý những bước gì | Lọc các `kc_code` có tần suất học viên trả lời sai lần đầu cao hoặc hay tua lùi trong `data/preclass` · Tóm tắt lại mỗi đoạn trong 2–4 câu bám sát ý chính + gán mã đoạn chuẩn + thiết kế câu hỏi kiểm tra hiểu tại checkpoint và tiêu chí chấm |
| Số dòng / số đoạn | ~12–15 đoạn kiến thức cốt lõi thuộc Day01 (`AI LLM Foundation`) và Day02 (`AI Problem Definition`), bao phủ toàn bộ 22 câu thử `C01`–`C22` |
| Phiên bản / ngày lấy | v1.0 — 27/11/2026 (dựng cho CP2 & hoàn thiện file JSON/CSV trong `data/` cho CP3) |
| Nhãn | `synthetic` (dựng bám sát danh mục `kc_code` thật của khoá học, đã kiểm tay 100%) |
| Giới hạn | Mới bao phủ 2 bài đầu (Day01, Day02) của chương trình để phục vụ bản chạy thử và bộ câu thử 22 câu; các đoạn văn là bản tóm tắt ý chính chứ không phải toàn bộ transcript dài hàng chục phút của video gốc |

**Data `synthetic` (nhóm tự sinh):** Nhóm biên tập thủ công dựa trên danh sách mã `ref` và `kc_code` trích từ `data/preclass/answers.csv` và `events.csv` (không sinh tự động hàng loạt bằng LLM). Người kiểm: Chu Mai Hồng & Nguyễn Hoàng Tùng đã kiểm tay 100% các đoạn và đối chiếu với 22 câu trong `eval/benchmark.csv`. Data tự dựng này dùng để vận hành công cụ tra cứu và kiểm thử Agent, **không phải bằng chứng pain**.

## Dataset 2 · Nhật ký hành vi học tập `data/preclass` (BTC cấp)

| | |
|---|---|
| Dùng để làm gì | Đào bằng chứng pain (`evidence/data-mining.md` qua `evidence/count.py`, tổng hợp tại `evidence/summary.md`) · Rút ra 8/22 tình huống `data_that` trong `eval/benchmark.csv` (`C02`, `C03`, `C04`, `C06`, `C07`, `C13`, `C15`, `C17`) |
| Từ đâu | Data BTC cấp trong repo đề (`../K5-L3-Day15-AI-Product-Hackathon/data/preclass`: `learners.csv`, `events.csv`, `answers.csv`, `chat.csv`, `column_dictionary.csv`, `event_types.csv`) — **không commit nguyên file vào repo nộp bài** |
| Xử lý những bước gì | Lọc học viên có hoạt động (`436/721`) và học viên mở video (`431/436`) · Đếm lượt tua lùi (`to < from` trên `video_seeked`), lượt mở lại video (`open_count >= 2`), lượt đóng bỏ qua quiz (`skipped_stop = True`), tỉ lệ sai lần đầu (`lan_thu = 1`, `was_correct = False`) theo từng nguồn (`pre_post_post`, `thuc_hanh`) · Giữ nguyên mã ẩn danh (`Lxxxx`, `Axxxxx`, `Cxxxxx`) (script: `evidence/count.py`) |
| Số dòng / số đoạn | `721` dòng `learners.csv` (`436` học viên có hoạt động) · `107.709` dòng `events.csv` · `3.776` dòng `answers.csv` · `1.260` dòng `chat.csv` |
| Phiên bản / ngày lấy | Log từ `05/11/2026` đến `25/11/2026` (Day01 → Day13), truy xuất ngày `27/11/2026` |
| Nhãn | `thật` (log hành vi thực tế trên `preclass-online.com` đã được BTC ẩn danh) |
| Giới hạn | (1) Không có nội dung chữ học viên gõ trong câu trả lời hay khung chat (chỉ có độ dài ký tự `do_dai_cau_hoi`), nên biết học viên tua lùi/sai câu nào nhưng không thấy nguyên văn câu chữ họ diễn đạt; (2) `answers.csv` mới ghi `7` dòng `video_quiz` (trong khi `events.csv` có `2.153` lượt `quiz_item_opened`) và `checkpoint_presented` có `0` dòng vì tính năng checkpoint chưa bật trong đợt thu thập log này |
