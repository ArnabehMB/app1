from http.server import SimpleHTTPRequestHandler, HTTPServer

class HelloHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello, World!")

if __name__ == "__main__":
    server_address = ('', 80)
    httpd = HTTPServer(server_address, HelloHandler)
    print("Server running on port 80...")
    httpd.serve_forever()

