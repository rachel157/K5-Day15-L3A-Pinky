"""Vercel Function for the same demo API served by Render."""
from urllib.parse import parse_qs, urlsplit

from demo.demo_server import Handler, VIDEO_PATH


ROUTES = {
    "health": "/api/health",
    "lesson": "/api/lesson",
    "answer": "/api/answer",
    "chat": "/api/chat",
    "video": VIDEO_PATH,
}


class handler(Handler):
    def _set_api_path(self):
        url = urlsplit(self.path)
        if url.path == "/api/dispatch":
            self.path = ROUTES.get(parse_qs(url.query).get("endpoint", [""])[0], "")
        else:
            self.path = url.path
        if self.path in ROUTES.values():
            return True
        self.send_error(404)
        return False

    def do_GET(self):
        if self._set_api_path():
            super().do_GET()

    def do_HEAD(self):
        if self._set_api_path():
            super().do_HEAD()

    def do_POST(self):
        if self._set_api_path():
            super().do_POST()
