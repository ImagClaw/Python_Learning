#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: (SERVER) Create a tcp server/client that does a file transfer.
#   Date: 5/2/2019

import socket, threading, sys, os


def main():
    host = str(sys.argv[1])
    port = int(sys.argv[2])


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind((host, port))
    print("\n[+] Starting server on {} port {}".format(host, port))
    s.listen(5)
    conn, addr = s.accept()
    print(" [-] Connection received from {}".format(addr[0]))

    file_name = "bullyingBeasley.txt"
    print(' [-] File name: {}'.format(file_name))
    print(' [-] File size: {} bytes'.format(str(os.path.getsize(file_name))))

    
    with open(file_name, 'rb') as file:
        data = file.read()
        conn.sendall(data)
    
        s.close()

        print(" [-] File sent Successfully")
        sys.exit(0)


if __name__ == "__main__":
    main()