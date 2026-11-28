# Triển khai Checkpoint Tutor

Nhánh triển khai: `chore/deploy`. Hai bản dùng cùng mã Python và dữ liệu bài học.
Render chạy máy chủ demo. Vercel phục vụ giao diện tĩnh và chuyển tiếp các API
nội bộ đến Vercel Function. Cả hai dùng Python 3.12.

## Render

Tạo Blueprint từ repo, chọn nhánh `chore/deploy` và đặt Blueprint Path thành
`infra/render.yaml`. Blueprint
tạo web service `pinky-checkpoint-tutor` ở Singapore theo gói Free, chạy
`python demo/demo_server.py` trên cổng Render cấp và kiểm tra `/api/health`.
[Render Blueprint](https://render.com/docs/blueprint-spec)

## Vercel

Dùng thư mục gốc repo. `vercel.json` chọn framework Other, build giao diện bằng
`node scripts/build-vercel.mjs` và xuất HTML vào `dist/`. Các route API và video
đi qua `api/dispatch.py`.

Tạo Preview từ nhánh `chore/deploy` bằng Git integration hoặc `vercel deploy`.
Chỉ chọn nhánh này làm Production Branch khi muốn đưa bản demo lên miền
production. [Quy trình Vercel CLI](https://vercel.com/docs/projects/deploy-from-cli)

## Biến môi trường

| Tên | Giá trị |
|---|---|
| `MODEL_PROVIDER` | Mặc định `fake` để thử giao diện và API. Đặt `openai`, `gemini` hoặc `anthropic` khi muốn gọi model thật. |
| `MODEL_NAME` | Tên model do provider hỗ trợ. Cấu hình đã dùng để eval là `gpt-5.4-mini`. |
| `API_KEY` | Khóa model, lưu dưới dạng bí mật trong Environment Variables của nền tảng tương ứng. |
| `DEMO_VIDEO_URL` | URL HTTPS của video MP4 được phép dùng. Máy chủ chuyển hướng yêu cầu từ trình phát sang URL này nếu không có file MP4 local. |

Video dùng khi chạy local có thể đặt tại `demo/assets/agent-video-internal-demo.mp4`.
Các bản cloud cần `DEMO_VIDEO_URL` để phát video.

## Kiểm tra và quay lui

- Mở `/` và gọi `GET /api/health`, `GET /api/lesson`. Health trả về status
  `ok`, bài học có danh sách đoạn.
- Gửi `{"answer":"ok"}` đến `POST /api/answer` để xem nhánh hỏi làm rõ.
  Khi đã cấu hình model thật, kiểm tra thêm một câu cần gợi ý đoạn xem lại và
  xác nhận `trace.model_calls` lớn hơn 0.
- Nếu bản mới có lỗi, chọn lần triển khai ổn định trước đó trong danh sách
  Events của Render hoặc dùng `vercel rollback <deployment-url>` cho production
  trên Vercel. Sau đó chạy lại các bước kiểm tra trên.
  [Render rollback](https://render.com/docs/rollbacks) · [Vercel rollback](https://vercel.com/docs/cli/rollback)
