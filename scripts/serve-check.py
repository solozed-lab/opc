#!/usr/bin/env python3
import http.server, socketserver, os, sys, urllib.request, threading, time, functools

port =8772
root = sys.argv[1] if len(sys.argv) >1 else 'dist'
os.chdir(os.path.abspath(root))

handler = functools.partial(http.server.SimpleHTTPRequestHandler)
handler.log_message = lambda *a, **k: None
httpd = socketserver.TCPServer(('', port), handler)
print('serving', os.getcwd(), 'on', port, flush=True)
threading.Thread(target=httpd.serve_forever, daemon=True).start()
time.sleep(0.5)


def check():
	resp = urllib.request.urlopen('http://127.0.0.1:%d/' % port, timeout=3)
	body = resp.read().decode()
	print('status:', resp.status)
	print('content-type:', resp.headers.get('Content-Type'))
	markers = ['sr-only', 'application/ld+json', 'canonical', 'COMPOSING STILL', 'fetchpriority="high"', 'width="1672"', 'height="941"']
	for m in markers:
		print(' has', repr(m), ':', m in body)
	r = urllib.request.urlopen('http://127.0.0.1:%d/robots.txt' % port, timeout=3)
	print('--- robots.txt ---')
	print(r.read().decode())
	r = urllib.request.urlopen('http://127.0.0.1:%d/sitemap.xml' % port, timeout=3)
	print('--- sitemap.xml ---')
	print(r.read().decode())


try:
	check()
except Exception as e:
	print('error:', e)
