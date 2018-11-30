#   Vic Chimenti
#   CPSC 5510 FQ18
#   p2 Distributed Hash Table
#   dht_client.py
#   created         11/26/2018
#   last modified   11/29/2018
#   Distributed Hash Table Client
#   /usr/local/python3/bin/python3





import sys              # for system calls
import socket           # for udp socket functionality
import pickle           # for sending a list over socket
import struct           # for ip adress manipulation
import argparse         # for parsing command line arguments
import ipaddress        # create ipv4 tuple




#   ***************     function definitions     ***************   #


# get the hostname
def getHost() :
    try :
        h = socket.gethostname()
    except AttributeError :
        error_message = "ERROR Failed to Get Hostname"
        print (error_message)
        sys.exit ("Exiting Program")

    return h


# get the host IP number
def getIP(h) :
    try :
        h_ip = socket.gethostbyname(h)
    except AttributeError :
        error_message = "ERROR Failed to Get Host IP Number"
        print (error_message)
        sys.exit ("Exiting Program")

    return h_ip


# convert ip address string to long
def ipToLong (ip) :
    return struct.unpack('>L', socket.inet_aton(ip))[0]


# # get user input from command line
# def getInput (param) :
#     try :
#         user_input = sys.argv[param]
#     except IndexError :
#         sys.stderr.write ("ERROR No Valid Command Line Input : ")
#         sys.exit ("Exiting Program")
#     except KeyError :
#         sys.stderr.write ("ERROR Invalid Charcter Entered : ")
#         sys.exit ("Exiting Program")
#     except Exception :
#         sys.stderr.write ("ERROR Invalid Command Line Entry : ")
#         sys.exit ("Exiting Program")
#     return user_input


# # validate URL entered and assign host IP number
# def getIP(nd) :
#     try :
#         nd_ip = socket.gethostbyname(nd)
#     except socket.gaierror :
#         sys.stderr.write ("ERROR Invalid URL Entered : ")
#         sys.exit ("Exiting Program")
#
#     # convert host IP number to str for troubleshooting/testing
#     node_ip_str = str(nd_ip)
#     print ("node_ip_str : " + node_ip_str)
#     if node_ip_str == MATCH_ALL :
#             sys.stderr.write ("ERROR Invalid IP Number : ")
#             sys.exit ("Exiting Program")
#
#     return node_ip_str


#   ***************     end function definitions     ***************   #




# DEFINE CONTSANTS
MATCH_ALL = "0.0.0.0"       # for IP validity checking
MY_PORT = 10101             # pre-defined client port number

# define defaults
charset = "UTF-8"           # default encoding protocol

# parse and assign command-line input
parser = argparse.ArgumentParser()
parser.add_argument('node', type=str, nargs=1, default='cs1.seattleu.edu')
parser.add_argument('nodePort', type=int, nargs=1, default=10109)
parser.add_argument('operation', type=str, nargs=1)
parser.add_argument('key', type=str, nargs=1)
parser.add_argument('value', type=str, nargs='*', default='')
args = parser.parse_args()

print ('node : ' + str(args.node))
print ('nodePort : ' + str(args.nodePort))
print ('operation : ' + str(args.operation))
print ('key : ' + str(args.key))
print ('value : ' + str(args.value))



# TODO :
#   combine key value pair into single string
#   add ts print for message received in str format
#   clean and prep for encryption


# get local host info
my_URL = getHost()
my_IP = getIP(my_URL)
my_address = (my_IP, MY_PORT)

# connect to a node
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSock.bind(my_address)
ip_address, my_port = clientSock.getsockname()

# define host port number and node
server_address = (str(args.node[0]), int(args.nodePort[0]))

# compile key value pair for server request
request = my_IP, MY_PORT, args.operation[0], args.key[0], args.value[0]
message = pickle.dumps(request)
print ('message : ' + str(message))

# send key value pair
bytes_sent = clientSock.sendto(message, server_address)
print ('sent {} bytes to {}'.format(bytes_sent, str(args.node[0])))

# receive response
message, response_node = clientSock.recvfrom(4096)
response = pickle.loads(message)
print ('received {} bytes from {}'.format(len(response), response_node))
print ('response : ' + str(response))

clientSock.close()
print ('Socket Closed')
#   eof
