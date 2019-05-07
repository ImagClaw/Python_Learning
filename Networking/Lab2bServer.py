import socket, json, sys


def main():
    host = 'localhost'
    port = 8080
    buf = 4096

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print('Starting up on %s port %s' % (host, port))
    s.bind((host, port))
    while True:
        data, _ = s.recvfrom(buf)
        print("Json data: ", data)
        unjson = json.loads(data)
        print("Json data converted to dictionary: ", unjson)
    
    s.close()


if __name__ == "__main__":
    main()

