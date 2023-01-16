import time

import pyftpdlib
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import socket
import segno

print('wellcome to FTP server')


hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
port = 9999
print('ftp://'+ip+':9999/')
path = 'D:/'
print("default path is D:/")
addr = (ip, '9999')
user = "suchith"
pd = "1234"
authorizer = DummyAuthorizer()
authorizer.add_anonymous(path, perm='elradfmw')
# authorizer.add_user(user, pd, path, perm='elradfmw')
handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(addr, handler)
qr = ('ftp://'+ip+':9999/')
qrcode = segno.make_qr(qr)
qrcode.save('ip.png', scale=10)
print("Any enquiry contact developer at suchith.nanded@gmail.com")
time.sleep(5)
qrcode.show()
server.serve_forever()
