"""
Created on Wed Jun  9 13:34:44 2021

UDP_Socket_Server
TCP_Socket_Client
Gateway

@author: caste
"""
import socket as sk
import sys
import time



# Fuction which moves surveys from devices to gateway
def connectionToClientUDP (message, server_address, buffer_size):

    # UDP Server Pocket
    # Creating the object SOCKET
    socket_devices = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
    print ('\nStarting up on %s port %s' % server_address)
    # Associating the socket with the server_address
    socket_devices.bind(server_address)
    
    for i in range(4):
        # Waiting for receiving message
        print('\nWaiting to receive message...')
        data, address = socket_devices.recvfrom(4096)
        # Surveys received
        print('Received %s bytes from a Device' % (len(data)))
        message = message + data.decode('utf-8') + "\n"
        # Printing surveys
        print(message)
        # Waiting 2 seconds for reply
        time.sleep(2)
        # Reply with OK message to Device
        sent = socket_devices.sendto("Surveys arrived".encode(), address)
        print ('Sent %s bytes back to Device' % (sent))
        
    socket_devices.close()
    return message

# Fuction which moves surveys from gateway to cloud
def connectionToServerTCP (message, server_address, buffer_size):
    
    # TCP Server Pocket
    # Creating the object SOCKET
    socket_cloud = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    
    # Connecting to Cloud
    try:
        socket_cloud.connect(server_address)
        print("Sending surveys to Cloud... ")
        #Waiting 2 second for sending the request
        time.sleep(2)
        #Taking note about the current time for calculate the total_time
        time_zero = time.time()
        
    # If connection failed printing an error message
    except Exception as data:
        print (Exception,":",data)
        print ("Connection failed, try again.\r\n")
        sys.exit(0)
    
    # Sending surveys to cloud
    socket_cloud.send(message.encode()) 
    # Print message
    print(message.encode())   
    # Waiting for a response from the cloud
    print("Waiting the server's response...")
    response = socket_cloud.recv(buffer_size)
    # Taking note about the current time for calculate the total_time
    time_n = time.time()
    # Calculating the total time for sending surveys from gateway to cloud
    total_time = time_n - time_zero
    print("Received Message: {}" .format(response.decode("utf8")))
    print("TCP message's sending time {} and the size of used buffer is {}" .format(total_time, buffer_size))
    print("\nClosing connection\n")
    socket_cloud.close()    

# Information about the gateway in each interfaces
server_gateway_address = ('localhost', 10005)
buffer_size = 4096
message = ""
# Moving surveys from devices to gateway
message = connectionToClientUDP(message, server_gateway_address, buffer_size)
server_cloud_address = ('localhost', 8001)
# Moving surveys from gateway to cloud
connectionToServerTCP(message, server_cloud_address, buffer_size)
