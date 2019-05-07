import socket
import sys

def main():
    try:
        for res in socket.getaddrinfo(sys.argv[1], None, proto=socket.IPPROTO_TCP):
            sockaddr = res[4]
            print("The address is: {}".format(sockaddr[0]))
    except socket.gaierror:
        print("Invalid")


if __name__ == "__main__":
    main()