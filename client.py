import socket
import threading
import time
import argparse

tLock = threading.Lock()

shutdown = False

def receiving(name,sock):
	while not shutdown:
		try:
			tLock.acquire()
			while True:
				data, addr = sock.recvfrom(1024)
				print str(data)
		except :
			pass

		finally:
				tLock.release()

def getServerIp():
	parser = argparse.ArgumentParser()
	parser.add_argument("server_Ip",help="IP address of the Chat server you want to use", type = str)
	args = parser.parse_args()
	return args.server_Ip

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("gmail.com",80))
myIp = s.getsockname()[0]
s.close()
server = (getServerIp(),5000)

host = myIp

port = 0

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

rT = threading.Thread(target=receiving,args=("RevcThread",s))

rT.start()

alias = raw_input("Enter name: ")

message = raw_input(alias + ": ")

while message != 'q':
	if message != '':
		s.sendto(alias + ": " + message, server)
	tLock.acquire()
	message = raw_input(alias + ": ")
	tLock.release()
	time.sleep(0.2)

shutdown = True
rT.join()
s.close()