import socket


def main():
    host = '0.0.0.0'
    port = 8080
    buffer = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Starting socket on port: {}".format(port))

    s.bind((host, port))
    s.listen(10)

    conn, addr = s.accept()
    print("Connection received from {}".format(addr))

    data = conn.recv(buffer)
    print("Received: {}".format(data))

    reversed = data[::-1]

    conn.sendall(reversed)

    conn.close()

if __name__ == "__main__":
    main()