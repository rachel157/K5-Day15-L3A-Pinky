"""Công cụ đọc và đánh giá bài học mẫu của Checkpoint Tutor."""
import json
import os
import re
from typing import Any

from tracing import tool

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSON_PATH = os.path.join(ROOT, "data", "lesson.json")


def _load_lesson() -> dict:
    with open(LESSON_PATH, encoding="utf-8") as f:
        return json.load(f)


def _segments() -> list[dict]:
    return _load_lesson().get("segments", [])


def _tokens(text: str) -> set[str]:
    return {token.lower() for token in re.findall(r"[\wÀ-ỹ]+", text or "") if len(token) > 2}


@tool
def get_segment(segment_id: str) -> dict:
    """Lấy một đoạn bài học theo mã.
    Input: segment_id (str), ví dụ L01-S02.
    Output: đoạn có transcript, timestamp, khái niệm và rubric; hoặc error.
    Tác động ra ngoài: không, chỉ đọc dữ liệu demo.
    """
    for segment in _segments():
        if segment.get("id") == segment_id:
            return segment
    return {"error": "Không tìm thấy đoạn %s trong bài học." % segment_id}


@tool
def search_segments(query: str) -> list[dict]:
    """Tìm các đoạn liên quan bằng từ khóa.
    Input: query (str).
    Output: danh sách đoạn có title, transcript hoặc key_concepts trùng từ khóa.
    Tác động ra ngoài: không, chỉ đọc dữ liệu demo.
    """
    query_tokens = _tokens(query)
    scored = []
    for segment in _segments():
        haystack = " ".join([
            segment.get("title", ""),
            segment.get("transcript", ""),
            " ".join(segment.get("key_concepts", [])),
        ])
        score = len(query_tokens & _tokens(haystack))
        if score:
            scored.append((score, segment))
    scored.sort(key=lambda item: item[0], reverse=True)
    return [segment for _, segment in scored]


@tool
def evaluate_answer(segment_id: str, learner_answer: str) -> dict:
    """Đánh giá sơ bộ câu trả lời theo rubric của đoạn.
    Input: segment_id (str), learner_answer (str).
    Output: status (correct/partial/incorrect/unclear), ý còn thiếu và tỷ lệ ý khớp.
    Tác động ra ngoài: không, chỉ tính toán từ dữ liệu demo.
    """
    segment = get_segment(segment_id)
    if "error" in segment:
        return {"status": "unclear", "matched": 0, "total": 0, "missing": [], "error": segment["error"]}

    answer_tokens = _tokens(learner_answer)
    if len(answer_tokens) < 2:
        return {
            "status": "unclear",
            "matched": 0,
            "total": len(segment.get("rubric", [])),
            "missing": segment.get("rubric", []),
        }

    matched = []
    missing = []
    for criterion in segment.get("rubric", []):
        criterion_tokens = _tokens(criterion)
        overlap = len(answer_tokens & criterion_tokens)
        # Một ý được xem là có dấu hiệu được nêu nếu có ít nhất hai từ khóa trùng.
        if overlap >= 2 or criterion.lower() in learner_answer.lower():
            matched.append(criterion)
        else:
            missing.append(criterion)

    total = len(segment.get("rubric", [])) or 1
    ratio = len(matched) / total
    status = "correct" if ratio >= 0.75 else "partial" if ratio > 0 else "incorrect"
    return {"status": status, "matched": len(matched), "total": len(segment.get("rubric", [])), "missing": missing}


@tool
def build_review_report(results: list[dict]) -> dict:
    """Tổng hợp các lỗ hổng sau nhiều checkpoint hoặc bài kiểm tra cuối.
    Input: results, danh sách kết quả có segment_id, status và missing.
    Output: danh sách đoạn nên xem lại và các ý còn thiếu.
    Tác động ra ngoài: không, chỉ tổng hợp trong phiên học.
    """
    weak = [item for item in results if item.get("status") in {"partial", "incorrect", "unclear"}]
    report = []
    seen = set()
    for item in weak:
        segment_id = item.get("segment_id")
        if not segment_id or segment_id in seen:
            continue
        seen.add(segment_id)
        segment = get_segment(segment_id)
        report.append({
            "segment_id": segment_id,
            "title": segment.get("title", ""),
            "status": item.get("status"),
            "missing": item.get("missing", []),
            "suggestion": "Bạn có thể xem lại đoạn %s (%ss–%ss)." % (
                segment_id, segment.get("start_time", 0), segment.get("end_time", 0)
            ),
        })
    return {"weak_segments": report, "count": len(report)}
