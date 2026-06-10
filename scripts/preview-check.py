import http.server
import socketserver
import os
import threading
import urllib.request
import time

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dist'))
port =8769
handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(('', port), handler)
print('serving on', port, flush=True)
t = threading.Thread(target=httpd.serve_forever, daemon=True)
t.start()
time.sleep(1)
try:
	resp = urllib.request.urlopen('http://127.0.0.1:%d/' % port, timeout=3)
	print('status:', resp.status)
	print('content-type:', resp.headers.get('Content-Type'))
	body = resp.read().decode()
	markers = ['sr-only', 'application/ld+json', 'canonical', 'COMPOSING STILL']
	for m in markers:
		print('has', repr(m), ':', m in body)
except Exception as e:
	print('error:', e)
