import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("gmail.com",80))
myIp = s.getsockname()[0]
s.close()
host = myIp
port = 5000

clients = []

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind((host,port))

s.setblocking(0)

quitting = False

print "Server Started"

while not quitting:
	try:
		data, addr = s.recvfrom(1024)
		if "Quit" in str(data):
			quitting = True
		elif addr not in clients:
			clients.append(addr)

		print time.ctime(time.time()) + str(addr) + ": : " + str(data)

		for client in clients:
			if client != addr:
				s.sendto(data, client)
	except:
		pass

s.close()
	
