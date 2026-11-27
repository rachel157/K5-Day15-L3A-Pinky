"""Script đào dữ liệu hành vi thật trên bộ data/preclass (Track A).

Chạy lại để kiểm chứng số trong evidence/data-mining.md:
    python evidence/count.py --data-dir ../K5-L3-Day15-AI-Product-Hackathon/data/preclass

Chỉ dùng thư viện chuẩn Python. Không ghi lại hay sao chép file dữ liệu gốc.
"""
import argparse
import csv
import json
import os
import sys
from collections import Counter, defaultdict

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

DEFAULT_CANDIDATES = [
    os.path.join("data", "preclass"),
    os.path.join("..", "K5-L3-Day15-AI-Product-Hackathon", "data", "preclass"),
]


def resolve_data_dir(cli_path: str | None) -> str:
    """Tìm thư mục chứa data/preclass từ tham số hoặc vị trí mặc định."""
    if cli_path:
        if os.path.isdir(cli_path):
            return os.path.abspath(cli_path)
        raise FileNotFoundError(f"Không tìm thấy thư mục: {cli_path}")
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for rel in DEFAULT_CANDIDATES:
        candidate = os.path.abspath(os.path.join(root, rel))
        if os.path.isfile(os.path.join(candidate, "events.csv")):
            return candidate
    raise FileNotFoundError(
        "Không tìm thấy data/preclass. Truyền đường dẫn bằng --data-dir <path>."
    )


def pct(x: int, n: int) -> str:
    """Định dạng chuẩn x/N (y%)."""
    if n == 0:
        return "0/0 (0.0%)"
    return f"{x}/{n} ({(x / n) * 100:.1f}%)"


def read_csv(path: str):
    """Đọc CSV UTF-8 theo từng dòng dict."""
    with open(path, encoding="utf-8-sig", newline="") as f:
        yield from csv.DictReader(f)


def parse_json(raw: str) -> dict:
    """Parse cột data JSON trong events.csv an toàn."""
    if not raw:
        return {}
    try:
        obj = json.loads(raw)
        return obj if isinstance(obj, dict) else {}
    except json.JSONDecodeError:
        return {}


def main() -> int:
    parser = argparse.ArgumentParser(description="Đếm bằng chứng pain từ data/preclass")
    parser.add_argument("--data-dir", help="Đường dẫn tới thư mục data/preclass")
    args = parser.parse_args()

    data_dir = resolve_data_dir(args.data_dir)
    print(f"Đọc dữ liệu từ: {data_dir}\n")

    # 1. Đọc learners.csv (tổng tài khoản)
    all_learners = {row["hv"] for row in read_csv(os.path.join(data_dir, "learners.csv"))}

    # 2. Quét events.csv
    active_learners = set()
    video_learners = set()
    video_open_rows = 0
    video_reopen_rows = 0
    video_reopen_learners = set()
    video_ended_rows = 0
    video_ended_learners = set()

    seek_rows = 0
    seek_back_rows = 0
    seek_fwd_rows = 0
    seek_crossed_stop_rows = 0
    seek_learners = set()
    seek_back_learners = set()
    seek_crossed_learners = set()

    quiz_opened_rows = 0
    quiz_opened_learners = set()
    quiz_dismissed_rows = 0
    quiz_skipped_rows = 0
    quiz_dismissed_learners = set()
    quiz_skipped_learners = set()

    flush_rows = 0
    flush_fast_rows = 0
    flush_learners = set()
    flush_fast_learners = set()

    event_type_counts = Counter()

    ex_seek_back = []
    ex_crossed_stop = []
    ex_quiz_skipped = []
    ex_fast_rate = []

    for idx, row in enumerate(read_csv(os.path.join(data_dir, "events.csv")), start=2):
        hv = row["hv"]
        etype = row["type"]
        event_type_counts[etype] += 1
        if hv:
            active_learners.add(hv)

        payload = parse_json(row.get("data", ""))

        if etype == "video_opened":
            video_open_rows += 1
            video_learners.add(hv)
            open_count = payload.get("open_count")
            if isinstance(open_count, (int, float)) and open_count >= 2:
                video_reopen_rows += 1
                video_reopen_learners.add(hv)

        elif etype == "video_ended":
            video_ended_rows += 1
            video_ended_learners.add(hv)

        elif etype == "video_seeked":
            seek_rows += 1
            seek_learners.add(hv)
            frm = payload.get("from")
            to = payload.get("to")
            crossed = payload.get("crossed_stop") is True
            if isinstance(frm, (int, float)) and isinstance(to, (int, float)):
                if to < frm:
                    seek_back_rows += 1
                    seek_back_learners.add(hv)
                    if len(ex_seek_back) < 3:
                        ex_seek_back.append(
                            f"events.csv:{idx} | {hv} | video={row['video'] or '-'} | tua lùi {frm:.1f}s -> {to:.1f}s (at {row['occurred_at']})"
                        )
                elif to > frm:
                    seek_fwd_rows += 1
            if crossed:
                seek_crossed_stop_rows += 1
                seek_crossed_learners.add(hv)
                if len(ex_crossed_stop) < 3:
                    ex_crossed_stop.append(
                        f"events.csv:{idx} | {hv} | video={row['video'] or '-'} | tua qua câu hỏi {frm}s -> {to}s (crossed_stop=True)"
                    )

        elif etype == "quiz_item_opened":
            quiz_opened_rows += 1
            quiz_opened_learners.add(hv)

        elif etype == "quiz_item_dismissed":
            quiz_dismissed_rows += 1
            quiz_dismissed_learners.add(hv)
            if payload.get("skipped_stop") is True:
                quiz_skipped_rows += 1
                quiz_skipped_learners.add(hv)
                if len(ex_quiz_skipped) < 3:
                    ex_quiz_skipped.append(
                        f"events.csv:{idx} | {hv} | video={row['video'] or '-'} | q={payload.get('question_id')} | skipped_stop=True"
                    )

        elif etype == "video_segments_flushed":
            flush_rows += 1
            flush_learners.add(hv)
            rate = payload.get("last_rate")
            if isinstance(rate, (int, float)) and rate > 1:
                flush_fast_rows += 1
                flush_fast_learners.add(hv)
                if len(ex_fast_rate) < 2:
                    ex_fast_rate.append(
                        f"events.csv:{idx} | {hv} | video={row['video'] or '-'} | last_rate={rate}x"
                    )

    # 3. Quét answers.csv (chỉ tính lần thử đầu lan_thu == 1 và có was_correct True/False)
    ans_first_total = Counter()
    ans_first_wrong = Counter()
    ans_learners_total = defaultdict(set)
    ans_learners_wrong = defaultdict(set)
    ex_wrong_answers = []

    for idx, row in enumerate(read_csv(os.path.join(data_dir, "answers.csv")), start=2):
        nguon = row["nguon"]
        lan_thu = row.get("lan_thu", "").strip()
        wc = row.get("was_correct", "").strip()
        hv = row["hv"]
        if lan_thu == "1" and wc in ("True", "False"):
            ans_first_total[nguon] += 1
            ans_learners_total[nguon].add(hv)
            if wc == "False":
                ans_first_wrong[nguon] += 1
                ans_learners_wrong[nguon].add(hv)
                if nguon in ("video_quiz", "pre_post_post", "thuc_hanh") and len(ex_wrong_answers) < 5:
                    ex_wrong_answers.append(
                        f"answers.csv:{idx} | id={row['id']} | {hv} | nguon={nguon} | ref={row['ref']} | lan_thu=1 | was_correct=False"
                    )

    # 4. Quét chat.csv (hỏi trợ giảng AI dưới video)
    chat_rows = 0
    chat_video_q_rows = 0
    chat_learners = set()
    chat_video_q_learners = set()
    for row in read_csv(os.path.join(data_dir, "chat.csv")):
        chat_rows += 1
        hv = row["hv"]
        chat_learners.add(hv)
        if row["channel"] == "video_question":
            chat_video_q_rows += 1
            chat_video_q_learners.add(hv)

    print("=== 1. MẪU SỐ TỔNG QUAN ===")
    print(f"- Tổng tài khoản (learners.csv): {len(all_learners)}")
    print(f"- Học viên có hoạt động (events.csv): {pct(len(active_learners), len(all_learners))}")
    print(f"- Học viên từng mở video (video_opened / active): {pct(len(video_learners), len(active_learners))}")
    print(f"- Học viên từng xem hết ít nhất 1 video (video_ended / video_learners): {pct(len(video_ended_learners), len(video_learners))}")
    print(f"- Tổng lượt mở video (video_opened): {video_open_rows} | Tổng lượt xem hết video (video_ended): {video_ended_rows}")

    print("\n=== 2. HÀNH VI XEM VIDEO & TƯƠNG TÁC CÂU HỎI GIỮA VIDEO ===")
    print(f"- Mở lại video >= 2 lần (trên tổng lượt video_opened): {pct(video_reopen_rows, video_open_rows)}")
    print(f"- Học viên từng mở lại video >= 2 lần (trên video_learners): {pct(len(video_reopen_learners), len(video_learners))}")
    print(f"- Lượt xem tốc độ > 1x (trên lượt video_segments_flushed): {pct(flush_fast_rows, flush_rows)}")
    print(f"- Học viên từng xem tốc độ > 1x (trên flush_learners): {pct(len(flush_fast_learners), len(flush_learners))}")
    print(f"- Lượt tua lùi tìm lại đoạn (to < from / tổng video_seeked): {pct(seek_back_rows, seek_rows)}")
    print(f"- Lượt tua tiến (to > from / tổng video_seeked): {pct(seek_fwd_rows, seek_rows)}")
    print(f"- Học viên từng tua lùi video (trên video_learners): {pct(len(seek_back_learners), len(video_learners))}")
    print(f"- Lượt tua xuyên qua câu hỏi giữa video (crossed_stop=True / tổng video_seeked): {pct(seek_crossed_stop_rows, seek_rows)}")
    print(f"- Học viên từng tua qua câu hỏi giữa video (trên video_learners): {pct(len(seek_crossed_learners), len(video_learners))}")
    print(f"- Lượt đóng câu hỏi giữa video mà bỏ qua không trả lời (skipped_stop=True / quiz_item_dismissed): {pct(quiz_skipped_rows, quiz_dismissed_rows)}")
    print(f"- Học viên từng bỏ qua câu hỏi giữa video (trên quiz_opened_learners): {pct(len(quiz_skipped_learners), len(quiz_opened_learners))}")

    print("\n=== 3. TỈ LỆ TRẢ LỜI SAI NGAY LẦN ĐẦU (lan_thu = 1, có chấm đúng/sai) ===")
    for nguon in sorted(ans_first_total):
        tot = ans_first_total[nguon]
        wrg = ans_first_wrong[nguon]
        l_tot = len(ans_learners_total[nguon])
        l_wrg = len(ans_learners_wrong[nguon])
        print(f"- [{nguon}] Theo lượt trả lời sai lần 1: {pct(wrg, tot)} | Theo học viên từng sai lần 1: {pct(l_wrg, l_tot)}")

    print("\n=== 4. HỎI TRỢ GIẢNG AI DƯỚI VIDEO (chat.csv) ===")
    print(f"- Lượt hỏi trực tiếp dưới video/slide (video_question / tổng chat): {pct(chat_video_q_rows, chat_rows)}")
    print(f"- Học viên từng hỏi trợ giảng dưới video (trên video_learners): {pct(len(chat_video_q_learners), len(video_learners))}")

    print("\n=== 5. VÍ DỤ CỤ THỂ ĐÃ ẨN DANH (CHỌN >= 5 DÒNG ĐƯA VÀO evidence/data-mining.md) ===")
    for label, items in (
        ("Tua lùi video (tìm lại đoạn)", ex_seek_back),
        ("Tua qua câu hỏi giữa video", ex_crossed_stop),
        ("Bỏ qua câu hỏi giữa video", ex_quiz_skipped),
        ("Xem tốc độ nhanh > 1x", ex_fast_rate),
        ("Trả lời sai lần đầu", ex_wrong_answers),
    ):
        print(f"[{label}]")
        for item in items:
            print(f"  - {item}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
