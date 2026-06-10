#!/usr/bin/env python3
import http.server, socketserver, os, sys
port =8771
root = sys.argv[1] if len(sys.argv) >1 else 'dist'
os.chdir(os.path.abspath(root))
httpd = socketserver.TCPServer(('', port), http.server.SimpleHTTPRequestHandler)
print('serving', os.getcwd(), 'on', port, flush=True)
httpd.serve_forever()
