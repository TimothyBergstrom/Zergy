import sys, os, time

a=os.popen('netstat -b|find "http"').read()
print(r"\http connections" + a)
input('')


'''
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_TCP)

while True:
    print(s.recvfrom(65565))
'''
