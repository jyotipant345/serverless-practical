

from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        message = "Hello Student! Welcome to Serverless Computing."
        self.wfile.write(message.encode("utf-8"))


# Write your Python code here
