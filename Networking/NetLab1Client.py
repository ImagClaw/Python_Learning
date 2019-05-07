#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: Network byte order: Convert integers to and from host to network byte orderFunctions to consider in the “socket” module: ntohl()/htonl().
#   Date: 5/2/2019


import socket

def main():
    server_address = ('localhost', 8081)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(server_address)

    data = int(input("Enter a number: "))
    convdata = socket.ntohl(data)

    print(convdata)

    s.send(str(convdata).encode())
    newdata = s.recv(1024)
    print(newdata)

    s.close()

if __name__ == "__main__":
    main()

 