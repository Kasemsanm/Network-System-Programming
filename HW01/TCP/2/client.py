#!/usr/bin/env python

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 30000

f_img = open('photo.png','rb')
img = f_img.read()
f_img.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(img)
data = s.recv(BUFFER_SIZE)
s.close()

print "received data:", data
