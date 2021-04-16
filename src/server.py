import http.server
import os
import socketserver

HOST = os.environ.get('SERVER_HOST', "")
PORT = os.environ.get('SERVER_PORT', 9001)

class DefaultHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
 
with socketserver.TCPServer((HOST, PORT), DefaultHttpRequestHandler) as httpd:
    print("Serving HTTP server on port", PORT)
    httpd.serve_forever()
