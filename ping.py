from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class Serv(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()


    def do_GET(self):
        self._set_headers()
        self.wfile.write(bytes("pong", 'utf-8'))


httpd = HTTPServer(('localhost', 8080), Serv)
httpd.serve_forever()