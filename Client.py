# Name: Saipriya Thirvakadu, Student ID: 1001373543
# Client.py

import socket                   # Import socket module
import sys                      # Import sys module
import time                     # Import time module

s = socket.socket()             # Prepare a socket
port = 8080                     # Provide the port number
print("Hostname:", socket.gethostname())    # Print hostname of the server
print("Port: ", port)                       # Print the port number
host = sys.argv[1]                          # Read argv[1] from the command line
print(host)                                 # Print host
port_no = int(sys.argv[2])                  # Read argv[2] from the command line
print(port_no)                              # Print port number
filename = sys.argv[3]                      # Read argv[3] from the command line
print(filename)                             # Print the file name

s.connect((host, port_no))                  # Connect to the server which is listening to the mentioned port number
print("Connected to Server")                # Print a confirmation message
print("Peer name: "+str(s.getpeername()))   # Get the name of the peer (server) which its connected to
s.send(b'data /'+filename.encode())         # Request for a file from the server

t0 = time.time()                            # 't0' stores the time once the request for the file is initiated
while True:                                 # Initiate a process to receive the data
    data = s.recv(1024)                     # Read 1024 bytes of data and store it in 'data' variable
    if not data:                            # If there is no data, break the loop
        break
    print(data)                             # Print the data
print('Successfully received the file')     # Print a confirmation that the file has been received

t1 = time.time()                            # 't1' stores the time once the file is received
rtt = t1 - t0                               # Calculate the Round trip time
print("Round Trip Time: "+str(rtt)+"Secs")  # Print RTT
print('Socket Family: '+str(s.family))      # Print Socket Family of the server
print('Socket Protocol: '+str(s.proto))     # Print Socket Protocol of the server
print('Socket Type: '+str(s.type))          # Print Socket Type of the server
print('Time out: '+str(s.timeout))          # Print Time out value of the server

s.close()                                   # Close the socket
print('connection closed')                  # Print a confirmation message that the connection has been closed