#!/usr/bin/env python3
import http.server, socketserver, os, sys
port =8773
root = sys.argv[1] if len(sys.argv) >1 else 'dist'
os.chdir(os.path.abspath(root))
handler = http.server.SimpleHTTPRequestHandler
handler.log_message = lambda *a, **k: None
httpd = socketserver.TCPServer(('', port), handler)
print('serving', os.getcwd(), 'on', port, flush=True)
httpd.serve_forever()
