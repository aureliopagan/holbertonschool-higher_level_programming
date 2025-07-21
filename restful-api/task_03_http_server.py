from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _send_response(self, status_code=200, content_type='application/json'):
        """Helper to set headers and response code."""
        self.send_response(status_code)
        self.send_header('Content-Type', content_type)
        self.end_headers()

    def do_GET(self):
        """Handle GET requests for various endpoints."""
        if self.path == '/':
            self._send_response(200, 'text/plain')
            message = 'Hello, this is a simple API!'
            self.wfile.write(message.encode('utf-8'))

        elif self.path == '/data':
            data_payload = {
                'name': 'John',
                'age': 30,
                'city': 'New York'
            }
            self._send_response(200, 'application/json')
            self.wfile.write(json.dumps(data_payload).encode('utf-8'))

        elif self.path == '/status':
            self._send_response(200, 'text/plain')
            self.wfile.write(b'OK')

        elif self.path == '/info':
            info_payload = {
                'version': '1.0',
                'description': 'A simple API built with http.server'
            }
            self._send_response(200, 'application/json')
            self.wfile.write(json.dumps(info_payload).encode('utf-8'))

        else:
            # Path not recognized
            self._send_response(404, 'text/plain')
            self.wfile.write(b'Endpoint not found')

def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    server_address = ('', port)
    server = server_class(server_address, handler_class)
    print(f"Server is running on port {port}...")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
        print("Server stopped.")

if __name__ == '__main__':
    run()
