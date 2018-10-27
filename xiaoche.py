import socket
import motor


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(("192.168.1.143", 9901))

def reveice_play(s):
	data,addr = s.recvfrom(64000)
	print(data)

if __name__ == '__main__':

        while True:
            data,addr = s.recvfrom(64000)

            a = data.split()

            s1 = int(a[0])
            s2 = int(a[1])
            print(s1,s2)
            motor.speed_1(s1)
            motor.speed_2(s2)

    
