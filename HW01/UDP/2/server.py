import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

def fac(n):
    if n <= 1:
        return n
    return n*fac(n-1)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data
    print "fac of data :",str(fac(int(data)))
    if data:
        sent = sock.sendto(str(fac(int(data))), addr)
