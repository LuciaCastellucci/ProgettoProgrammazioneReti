# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 18:27:19 2021

UDP_Socket_Client
Device_2

@author: caste
"""

import GeneralDevice as device

# Taking note about Device informations
# Device IP
client_IP = "192.168.1.2"
# Gateway address
server_address = ("localhost", 10005)
# Buffer size
buffer_size = 4096
# Surveys file name
file_name = "Surveys2.txt"
# Reading surveys from file which contains surveys taken by Device 2
message = device.readingSurveys(file_name, client_IP)
# Connecting the client (device) with the server (gateway)
device.connectionToServerUDP(message, server_address, buffer_size)
