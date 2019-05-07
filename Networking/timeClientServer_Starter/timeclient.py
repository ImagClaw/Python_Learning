"""
File: timeclient.py
Client for obtaining the day and time.
"""

from socket import *
from codecs import decode
import errno

HOST = "localhost" 
PORT = 5000
BUFSIZE = 1024
ADDRESS = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)               # Create a socket
try:               
    server.connect(ADDRESS)                             # Create a socket
    dayAndTime = decode(server.recv(BUFSIZE), "ascii")  # Connect it to a host
    print(dayAndTime)                                   # Read a string from it
except Exception as errorMsg:
    if str(errno.ECONNREFUSED) in str(errorMsg):
        print("Server is not accepting connections.")
    else:
        raise
    
server.close()                                      # Close the connection
