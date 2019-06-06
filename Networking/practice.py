import re, socket

keys = ['5V&$10jr@y', 'As26yx*uTB', '5V8tY7&ox^']


def main():
    returnMsg = []
    PORT = 3000
    HOST = "10.128.102.115"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    s.connect((HOST, PORT))

    

    data2 = s.recv(1024)

    print(data2.decode())
    data = s.sendall(keys[1].encode())

    if data2.decode() == "Unrecognized command.":
        print("nope")
    
    print(data)


    received = s.recv(1024)
    print("Encoded data received:", received)

    # receives data and splits it every 2 chars.
    data = received.decode('utf-8')
    data = re.findall('..', data)
    
    # Iterates through keys
    for key in keys:
        keyConv = []
        msgConv = []
        text = []
        count = 0
        
        # Converts msg into decimal format
        for d in data:
            msgConv.append(int(d, 16))

        # Converts to decimal and appands
        for y in key:
            for x in y:
                keyConv.append(ord(x))
        
        for i in msgConv:
            key = keyConv[count]
            text.append(chr(i^key))
            count += 1
            if count >= len(keyConv):
                count = 0

        returnMsg.append(''.join(text))

        
    z = 0
    while z < len(returnMsg):
        print(returnMsg[z])
        s.sendall(str(returnMsg[z]).encode())
        data = s.recv(1024)
        print(data.decode())
        z += 1
    

    s.close()
        

if __name__ == "__main__":
    main()