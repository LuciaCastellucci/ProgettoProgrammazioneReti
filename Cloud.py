"""
Created on Wed Jun  9 13:34:44 2021

TCP_Socket_Server
Cloud_Server

@author: caste
"""
import socket as sk

def connectionToClientTCP():
    
    # TCP Server Pocket
    # Creating the object SOCKET
    serverSocket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    # Associating the socket with the server_address
    serverSocket.bind(server_address)

    # Define the backlog queue
    serverSocket.listen(1)
    # Now the socket is enable to receive connections
    print ('Cloud Server is waiting for connections...')
    
    # Starting loop
    while True:
        
        # The socket is enabled to reiceve connections
        print ('Cloud server is ready to serve...')
        # As soon as the connection is up, it returns a tuple
        connectionGateway, addr = serverSocket.accept()
        print('The Gateway is connected')
        # Printing the tuple returned
        print(connectionGateway,addr)

    try:
        # Receiving surveys from socket
        print('... And it is uploading the surveys')
        message = connectionGateway.recv(buffer_size)
        # Printing surveys
        print(message.decode("utf8"))
        # Reply with OK message to Gateway
        connectionGateway.send("Surveys received".encode())
        connectionGateway.send("\r\n".encode())
        # Closing connections with Gateway
        connectionGateway.close()
            
    
    except IOError:
        # Sending error message for file not found
        connectionGateway.send(bytes("HTTP/1.1 404 Not Found\r\n\r\n","UTF-8"))
        connectionGateway.send(bytes("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n","UTF-8"))
        connectionGateway.close()

# TCP port
server_address = ('localhost',8001)
print ('the web server is up on port:',8001)
# TCP IP address
server_IP = '10.10.10.2'
# Define buffer size on the trasmission channel
buffer_size = 4096
connectionToClientTCP()