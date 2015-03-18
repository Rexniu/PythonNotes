#!/usr/bin/env python

import socket

def convert_integer():
	data = 1234;
	# 32 bit
	print "Original:%s => Long host byte order: %s,Network byte order: %s" %(data,socket.ntohl(data),socket.htonl(data))
	print "Original:%s => Short host byte order:%s,Network byte order: %s" %(data,socket.ntohs(data),socket.ntohs(data))

if __name__ == "__main__":
	convert_integer()
