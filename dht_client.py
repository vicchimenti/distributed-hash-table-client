#   Vic Chimenti
#   CPSC 5510 FQ18
#   p2 Distributed Hash Table
#   dht_client.py
#   created         11/26/2018
#   last modified   12/1/2018
#   Distributed Hash Table Client
#   /usr/local/python3/bin/python3




import sys                  # for system calls
import socket               # for udp socket functionality
import pickle               # for sending a list over socket
import argparse             # for parsing command line arguments




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


#   ***************     end function definitions     ***************   #




# DEFINE CONTSANTS
MATCH_ALL = "0.0.0.0"       # for IP validity checking
MY_PORT = 10112             # pre-defined client port number

# define defaults
charset = "UTF-8"           # default encoding protocol
hops = 0                    # increments with each node hop


# ************* ADD ERROR CHECKING FOR GET WITH A VALUE *********** #

# parse and assign command-line input
parser = argparse.ArgumentParser()
parser.add_argument('node', type=str, nargs=1, default='cs1.seattleu.edu')
parser.add_argument('nodePort', type=int, nargs=1, default=10109)
parser.add_argument('operation', type=str, nargs=1)
parser.add_argument('key', type=str, nargs=1)
parser.add_argument('value', type=str, nargs='?', default='\n')
args = parser.parse_args()




# display user input
print ('\nnode : ' + str(args.node))
print ('nodePort : ' + str(args.nodePort))
print ('operation : ' + str(args.operation))
print ('key : ' + str(args.key))
print ('value : ' + str(args.value))




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


# ******************* TODO account for no value in value

# compile key value pair for server request
request = my_IP, MY_PORT, hops, args.operation[0], args.key[0], args.value[0]
message = pickle.dumps(request)




# send key value pair
bytes_sent = clientSock.sendto(message, server_address)
print ('\nsent {} bytes to {}'.format(bytes_sent, str(server_address)))
print ('request sent : ' + str(request))


# ******************* TODO: Format the Output Display ***********************  #

# receive response
message, response_node = clientSock.recvfrom(4096)
response = pickle.loads(message)
print ('\nreceived {} bytes from {}'.format(len(message), response_node))
print ('response received : ' + str(response))




clientSock.close()
print ('\nSocket Closed\n')
#   eof
