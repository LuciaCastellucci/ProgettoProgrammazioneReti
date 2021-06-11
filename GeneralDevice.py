# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 18:27:19 2021

Fuctions common to all devices

@author: caste
"""

import socket as sk
import time

# Function which connect the client (device) with the server (gateway)
# With an  UDP connection
def connectionToServerUDP (message, server_address, buffer_size):
    # UDP Server Pocket
    # Creating the object SOCKET
    socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
    # Sending surveys to Gateway
    try:
        print("Sending surveys to Gateway... ")
        # Waiting 2 second for sending the request
        time.sleep(2)
        # Taking note about the current time for calculate the total_time
        time_zero = time.time()
        # Sending the request
        socket.sendto(message.encode(), server_address)
        print('... Waiting to receive the response frome the Gateway...')
        # Receiving the response from server
        data, server = socket.recvfrom(buffer_size)
        # Taking note about the current time for calculate the total_time
        time_n = time.time()
        # Calculating total time
        total_time = time_n - time_zero
        # Waiting 2 seconds for printing the OK message
        time.sleep(2)
        print ('Received message! The message contains: "%s"' % data.decode('utf8'))
        print("UDP message's sending time {} and the size of used buffer is {}" .format(total_time, buffer_size))
        
    except Exception as info:
        print(info)
    
    finally:
        print("\nClosing socket\n")
        socket.close()
        
    

#Fuction which read surveys from file contained in the directory Surveys
def readingSurveys (file_name, client_IP):
    
    # Searching for file path
    filePath = "Surveys/" + file_name
    # Opening file witch contains surveys
    file = open(filePath, "r")
    print("Reading the detections from file...")
    # Waiting for the reading
    time.sleep(1)
    message = ""
    
    while True:
        # Reading line 
        line = file.readline()
        # If the file is over or the file is empty
        if (line == ""):
            # Let's stop the searching of surveys
            break;
        # If line is not empty
        else:
            # Let's format the message
            message =  message + client_IP + " " + line + "\n"
    
    # Closing the file
    file.close();
    print("Surveys readed!")
    
    return message


            
            
