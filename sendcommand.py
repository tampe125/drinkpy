import socket
import urllib
import urllib2
import json

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = (s.getsockname()[0])
s.close()

base_url = 'http://' + ip + ':9000/?commands='

params = {
    'stack': [
        {'motor1': 12},
        {'motor2': 22}
    ]
}

params = json.dumps(params)
params = urllib.quote_plus(params)

req = urllib2.Request(base_url + params)
response = urllib2.urlopen(req)
result = response.read()
