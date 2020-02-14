import pygame
from settings import Settings
import socket
import pygame.locals
import codecs
import time
import os
import sys
from numpy import interp
import math
import json



s = socket.socket()  # Create a socket object
port = 50000 # Reserve a port for your service every new transfer wants a new port or you must wait.

s.connect(('192.168.0.25', port))



data_list = [0,0]
while True:

    data = s.recv(1024)
    data = codecs.decode(data)
    c_d = data.split(" ")
    c_d = [x.replace("\r\n", "") for x in c_d]

    try:
        new_data = int(c_d[0])
        distance = int(c_d[1])
    except:
        continue



    data_list[0] = new_data
    data_list[1] = distance
    with open('data.txt', 'w') as new:
        lines = {}
        lines["distance_count"] = data_list
        json.dump(lines, new)

