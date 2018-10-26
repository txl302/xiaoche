import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(("192.168.1.143", 9901))

def reveice_play(s):
	data,addr = s.recvfrom(64000)
	print data

while True:
    reveice_play(s)

    