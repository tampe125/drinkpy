import socket
import urllib
import urllib2
import json

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = (s.getsockname()[0])
s.close()

# ip = '192.168.0.105'

base_url = 'http://' + ip + ':9000/?commands='

params = {
    'stack': [
        {1: 5},
        {2: 7}
    ]
}

params = json.dumps(params)
params = urllib.quote_plus(params)

req = urllib2.Request(base_url + params)
response = urllib2.urlopen(req)
result = response.read()
