#   Vic Chimenti
#   CPSC 5510 FQ18
#   p2 Distributed Hash Table
#   dht_client.py
#   created         11/26/2018
#   last modified   11/28/2018
#   Distributed Hash Table Client
#   /usr/local/python3/bin/python3







import socket
import sys
import argparse
#from inspect import signature


#   *****       *****   function definitions    *****       *****   #


# get user input from command line
def getInput (param) :
    try :
        user_input = sys.argv[param]
    except IndexError :
        sys.stderr.write ("ERROR No Valid Command Line Input : ")
        sys.exit ("Exiting Program")
    except KeyError :
        sys.stderr.write ("ERROR Invalid Charcter Entered : ")
        sys.exit ("Exiting Program")
    except Exception :
        sys.stderr.write ("ERROR Invalid Command Line Entry : ")
        sys.exit ("Exiting Program")
    return user_input


# validate URL entered and assign host IP number
def getIP(node)
    try :
        node_ip = socket.gethostbyname(node)
    except socket.gaierror :
        sys.stderr.write ("ERROR Invalid URL Entered : ")
        sys.exit ("Exiting Program")

    # convert host IP number to str for troubleshooting/testing
    node_ip_str = str(node_ip)
    print ("node_ip_str : " + node_ip_str)
    if node_ip_str == MATCH_ALL :
            sys.stderr.write ("ERROR Invalid IP Number : ")
            sys.exit ("Exiting Program")

    return node_ip_str


# command line signature
# def cmdLineSignature(self, arg1, kwarg1=None) :
#     pass

# TODO: add udp full functionality for sendto recvfrom and test with on cs1

# DEFINE CONTSANTS
PARAM_MIN = 3
PARAM_MAX = 4
MATCH_ALL = "0.0.0.0"                   # for IP validity checking

# set defaults
#port = 10109
#node = "cs1.seattleu.edu"
#operation = "get"
#key = "key"
#value = "value"
message = "Hello World"


# get the command line input
# sig = signature(cmdLineSignature)
# params = sig.parameters
# total_paramaters = len(params)

#***** TODO parse the command line parameters and assign to variables

parser = argparse.ArgumentParser()
parser.add_argument('node', type=str, nargs=1, default='cs1.seattleu.edu')
parser.add_argument('nodePort', type=int, nargs=1, default=10109)
parser.add_argument('operation', type=str, nargs=1, required=True)
parser.add_argument('key', type=str, nargs=1, required=True)
parser.add_argument('value', type=str, nargs='*', default='')



# connect to a node
ip_addr = getIP(node)
sock = socket.socket(socket.AF_INET, socket.SOCK_DRGAM)
sock.sento(message, (node, port))


#   eof
