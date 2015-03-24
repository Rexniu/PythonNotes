#!/usr/bin/env python

import urllib

URL = "https://www.github.com"
PROXY_ADDRESS = "165.24.10.8:8080" #By Googling free proxy server

if __name__ == '__main__':
	resp = urllib.urlopen(URL,proxies = {"http":PROXY_ADDRESS})
	print "Prxoy server returns response headers: %s " %resp.headers
