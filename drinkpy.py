import BaseHTTPServer
import socket
import urlparse

__author__ = 'tampe125'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8",80))
ip = (s.getsockname()[0])
s.close()

HOST_NAME = ip
PORT_NUMBER = 9000


class DrinkServer(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        """Respond to a GET request."""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("<html><head><title>Title goes here.</title></head>")
        self.wfile.write("<body><p>This is a test.</p>")

        qs = urlparse.parse_qs(urlparse.urlparse(self.path).query)

        self.wfile.write("<p>You accessed path: %s</p>" % qs)
        self.wfile.write("</body></html>")


if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), DrinkServer)
    print "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
