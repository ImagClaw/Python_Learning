#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: Network byte order: (SERVER) Convert integers to and from host to network byte orderFunctions to consider in the “socket” module: ntohl()/htonl().
#   Date: 5/2/2019
#

import socket

def main():
    host = 'localhost'
    port = 8081
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((host, port))
    s.listen()
    print("Starting server on {} port {}".format(host, port))

    conn, addr = s.accept()
    print("Connection received from {}".format(addr[0]))
    conn.send(b'Thanks for connecting.')

    data = conn.recv(1024)
    print("Byte data received: ", data)
    Int32InNetworkFormat = socket.htonl(int(data))
    
    conn.send(b'Your Network to Host Long number is: ' + str(Int32InNetworkFormat).encode())
    
    s.close()

if __name__ == "__main__":
    main()