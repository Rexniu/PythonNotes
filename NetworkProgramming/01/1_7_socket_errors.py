#!/usr/bin/env  python

import sys
import socket
import argparse

def main():
    #setup argument parsing
    parser = argparse.ArgumentParser(description='Socket Error Examples')
    parser.add_argument('--host',action="store",dest='host',required=False)
    parser.add_argument('--port',action="store",dest="port",type=int,required=False)
    parser.add_argument('--file',action="store",dest="file",required=False)

