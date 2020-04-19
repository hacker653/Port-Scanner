#!/usr/bin/python3

import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("Enter The IP You Want To Scan: ")
port = int(input("Enter The Port Number: "))

def Port_Scanner(port):
    if s.connect_ex((host, port)):
        print("The Port is Closed")
    else:
        print("The Port is Open")

Port_Scanner(port)

