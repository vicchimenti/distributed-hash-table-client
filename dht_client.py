#   Vic Chimenti
#   CPSC 5510 FQ18
#   p2 Distributed Hash Table
#   dht_client.py
#   created         11/26/2018
#   last modified   11/27/2018


#   Distributed Hash Table Client




import socket
import sys


# TODO: add udp full functionality for sendto recvfrom and test with on cs1

UDP_IP = "127.0.0.1"
UDP_PORT = 10109
MESSAGE = "Hello World"
sock = socket.socket(socket.AF_INET, socket.SOCK_DRGAM)
sock.sento(MESSAGE, (UDP_IP, UDP_PORT))


#   eof
