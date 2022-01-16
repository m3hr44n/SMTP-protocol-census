#!/usr/bin/python3

import socket
import sys

if len(sys.argv) !=2:

    print("How Use This Script ==> verfy.py <usernamr>")

    sys.exit(0)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connet = s.connect(('yor ip address',25))

banner = s.recv(1024)


print(banner)

s.send('VRFY' + sys.argv[1] + '\r\n')

result = s.recv(1024)

print(result)

s.close()
