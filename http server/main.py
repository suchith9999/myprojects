
import http.server
import socketserver
import socket
import segno
import time

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
PORT = 9999
handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    qr = ('http://' + ip + ':9999/')
    qrcode = segno.make_qr(qr)
    qrcode.save('ip.png', scale=10)
    print("Server started at localhost:" + qr)
    print("Any enquiry contact developer at suchith.nanded@gmail.com")
    time.sleep(5)
    qrcode.show()
    httpd.serve_forever()
