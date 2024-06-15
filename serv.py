#coding: utf-8

import http.server
import socketserver

port = 3000

address = ("", port)
handler = http.server.SimpleHTTPRequestHandler 
httpd = socketserver.TCPServer (address, handler)

print (f"Serveur démarré sur le PORT {port}")

httpd.serve_forever()