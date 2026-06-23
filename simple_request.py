from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs


# math functions
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b


class SimpleHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        url = urlparse(self.path)
        params = parse_qs(url.query)

        a = int(params['a'][0])
        b = int(params['b'][0])

        if url.path == '/add':
            res = add(a,b)
            op = 'addition'

        elif url.path == '/subtract':
            res = subtract(a,b)
            op = 'subtraction'

        elif url.path == '/multiply':
            res = multiply(a,b)
            op = 'multiplication'

        else:
            self.send_response(404)
            self.end_headers()
            return

        # build the response manually
        body = "{'a':" + str(a) + ", 'b':" + str(b) + ", 'operation':'" + op + "', 'result':" + str(res) + "}"

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(body.encode())

    # this is to stop the server from printing every request to the console
    def log_message(self, format, *args):
        pass


server = HTTPServer(('', 5000), SimpleHandler)
print('server started on port 5000')
server.serve_forever()
