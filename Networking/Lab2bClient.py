import socket, json



dictionary = {'this':'that', 'Birds':'bees','Girlfriend':'Wife'}

def main():
    server_address = ('localhost', 8080)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    print(dictionary) 
    jsondict = json.dumps(dictionary, indent=4)
    print("Sending data")
    print(jsondict)
    s.sendto(jsondict.encode(), server_address)

    s.close()

if __name__ == "__main__":
    main()