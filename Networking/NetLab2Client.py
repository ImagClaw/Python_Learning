#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: Create a program that finds the service name, the port and the protocol. 
#   Functions to consider in the “socket” module: getservbyport()
#   Date: 5/2/2019

import socket, sys

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = sys.argv[1]
    port = sys.argv[2]

    try:
        s.connect((str(host), int(port)))
        print("Port {}, is {}".format(port, socket.getservbyport(int(port), 'tcp')))
    except socket.error:
        print("Port doesn't exist. Try again dummy (Beasley).")

if __name__ == "__main__":
    main()