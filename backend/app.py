#!/usr/bin/env python3
"""Simple HTTP server for Effective Mobile test task."""

from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'Hello from Effective Mobile!')
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Not Found')
    
    def log_message(self, format, *args):
        """Logging to stdout for docker logs."""
        print(f"[Backend] {args[0]}")

def main():
    port = int(os.environ.get('PORT', 8080))
    server = HTTPServer(('0.0.0.0', port), RequestHandler)
    print(f"[Backend] Server started on port {port}")
    server.serve_forever()

if __name__ == '__main__':
    main()
