import http.server
import socket
import socketserver
import os
os.chdir('/home/suchith/')

print('http://' + socket.gethostbyname(socket.gethostname()) + ':9999/')
with socketserver.TCPServer(("", 9999), http.server.SimpleHTTPRequestHandler) as httpd:
    httpd.serve_forever()
