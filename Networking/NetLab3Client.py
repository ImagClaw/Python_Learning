#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: (CLIENT) Create a tcp server/client that does a file transfer.
#   Date: 5/2/2019

import socket, sys, threading

from time import sleep

def main():
    host = str(sys.argv[1])
    port = int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((host, port))

    data = s.recv(4096)
    f = open('beasley.txt', 'wb')

    while data != bytes(''.encode()):
        print(data)
        data = s.recv(1024)
        #f.write(data)

        f.writelines(data)


if __name__ == "__main__":
    main()