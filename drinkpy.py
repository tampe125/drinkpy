import BaseHTTPServer
import socket
import urlparse
from lib.pump import Pumps

__author__ = 'tampe125'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = (s.getsockname()[0])
s.close()

HOST_NAME = ip
PORT_NUMBER = 9000


class DrinkServer(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        """Respond to a GET request."""
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        qs = urlparse.parse_qs(urlparse.urlparse(self.path).query)

        self.wfile.write(qs)

        try:
            commands = qs['commands'][0]
        except KeyError:
            print "Empty command stack. Stopping here"
            return

        pumps = Pumps(commands)

    def log_message(self, format, *args):
        """Override standard logging to prevent too much output in console"""
        pass


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
