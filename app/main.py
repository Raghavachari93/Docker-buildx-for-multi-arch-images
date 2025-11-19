from http.server import BaseHTTPRequestHandler, HTTPServer
import os

PORT = int(os.environ.get("PORT", 8000))


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = "Hello from a multi-arch Docker image built with GitHub Actions + buildx!"
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))


if __name__ == "__main__":
    server = HTTPServer(("", PORT), Handler)
    print(f"Serving on port {PORT}")
    server.serve_forever()
