#   Vic Chimenti
#   CPSC 5510 FQ18
#   p2 Distributed Hash Table
#   dht_client.py
#   created         11/26/2018
#   last modified   12/6/2018
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
        exc = sys.exc_info()[1]
        print (exc)
        sys.exit ("Exiting Program")

    return h


# get the host IP number
def getIP(h) :
    try :
        h_ip = socket.gethostbyname(h)
    except AttributeError :
        error_message = "ERROR Failed to Get Host IP Number"
        print (error_message)
        exc = sys.exc_info()[1]
        print (exc)
        sys.exit ("Exiting Program")

    return h_ip


# if a value was entered with GET throw error and exit program
def validateOperator(op, v) :
    if op == GET :
        if v != NEWLINE :
            error_message = \
                "ERROR: GET request included value: all values invalid with GET"
            print (error_message)
            sys.exit ("Exiting Program")


#   ***************     end function definitions     ***************   #




# DEFINE CONTSANTS
MATCH_ALL = "0.0.0.0"       # for IP validity checking
MY_PORT = 10119             # pre-defined client port number
NEWLINE = '\n'              # newline constant
GET = 'get'                 # get operator
PUT = 'put'                 # put operator

# define defaults
charset = "UTF-8"           # default encoding protocol
hops = 0                    # increments with each node hop




# parse and assign command-line input
try :
    parser = argparse.ArgumentParser()
except SystemExit :
    print ('ERROR: Invalid Command Line Input: Please Re-run the Program')
    exc = sys.exc_info()[1]
    print (exc)
    sys.exit ('Exiting Program')
try :
    parser.add_argument('node', type=str, nargs=1, default='cs1.seattleu.edu')
except SystemExit :
    print ('ERROR: Invalid Command Line Input Node: Please Re-run the Program')
    exc = sys.exc_info()[1]
    print (exc)
    sys.exit ('Exiting Program')
try :
    parser.add_argument('nodePort', type=int, nargs=1, default=10109)
except SystemExit :
    print ('ERROR: Invalid Command Line Input NodePort: Please Re-run the Program')
    exc = sys.exc_info()[1]
    print (exc)
    sys.exit ('Exiting Program')
try :
    parser.add_argument('operation', type=str, nargs=1)
except SystemExit :
    print ('ERROR: Invalid Command Line Input Operation: Please Re-run the Program')
    exc = sys.exc_info()[1]
    print (exc)
    sys.exit ('Exiting Program')
try :
    parser.add_argument('key', type=str, nargs=1)
except SystemExit :
    print ('ERROR: Invalid Command Line Input Key: Please Re-run the Program')
    exc = sys.exc_info()[1]
    print (exc)
    sys.exit ('Exiting Program')
try :
    parser.add_argument('value', type=str, nargs='?', default=NEWLINE)
    args = parser.parse_args()
except SystemExit :
    print ('ERROR: Invalid Command Line Input Value: Please Re-run the Program')
    exc = sys.exc_info()[1]
    print (exc)
    sys.exit ('Exiting Program')




# check for user input of value with get request
validateOperator(args.operation[0], args.value[0])



# display user input
print ('\nnode : ' + str(args.node))
print ('nodePort : ' + str(args.nodePort))
print ('operation : ' + str(args.operation))
print ('key : ' + str(args.key))
print ('value : ' + str(args.value))




# get local host info
my_URL = getHost()
my_IP = getIP(my_URL)
try :
    my_address = (my_IP, MY_PORT)
except ValueError :
    print ('ERROR: Assigning Local Address')
    exc = sys.exc_info()[1]
    print (exc)
    sys.exit ("Exiting Program")




# connect to a node
try :
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except OSError :
    print ("ERROR Creating Socket")
    exc = sys.exc_info()[1]
    print (exc)
    sys.exit ("Exiting Program")

# bind to specific Port number
try :
    clientSock.bind(my_address)
except ConnectionError :
    print ('ERROR: ConnectionError Binding the Host and Port')
    exc = sys.exc_info()[1]
    print (exc)
    sys.exit ("Exiting Program")
except OSError :
    print ('ERROR Port Already in Use')
    exc = sys.exc_info()[1]
    print (exc)
    sys.exit ("Exiting Program")




# get my address info for send message
ip_address, my_port = clientSock.getsockname()

# define host port number and node
try :
    server_address = (str(args.node[0]), int(args.nodePort[0]))
except ValueError :
    print ('ERROR: Assigning Server Address')
    exc = sys.exc_info()[1]
    print (exc)
    sys.exit ("Exiting Program")




# compile key value pair for server request
try :
    request = my_IP, MY_PORT, hops, args.operation[0], args.key[0], args.value
except ValueError :
    print ('ERROR: Assigning Request Header')
    exc = sys.exc_info()[1]
    print (exc)
    sys.exit ("Exiting Program")

# pickle the message
try :
    message = pickle.dumps(request)
except PickleError :
    print ('ERROR: Pickling the Message')
    exc = sys.exc_info()[1]
    print (exc)
    sys.exit ("Exiting Program")




# send key value pair
try :
    bytes_sent = clientSock.sendto(message, server_address)
except OSError :
    print ('ERROR: Sending the Message')
    exc = sys.exc_info()[1]
    print (exc)
    sys.exit ("Exiting Program")
print ('\nsent {} bytes to {}'.format(bytes_sent, str(server_address)))
print ('\nrequest sent : \n' + str(request))




# receive response
try :
    message, response_node = clientSock.recvfrom(4096)
except OSError :
    print ('ERROR: Sending the Message')
    exc = sys.exc_info()[1]
    print (exc)
    sys.exit ("Exiting Program")

# unpickle the message
try :
    response = pickle.loads(message)
except UnpicklingError :
    print ('ERROR: UnPickling the Message')
    exc = sys.exc_info()[1]
    print (exc)
    sys.exit ("Exiting Program")
print ('\nreceived {} bytes from {}'.format(len(message), response_node))




# unpack and display response
key_hash, node_hash, total_hops, key_response, value_response = response
print ('\nThe hash of the Key : \n' + key_hash)
print ('\nThe hash of the Node : \n' + node_hash)
print ('\nThe total hops : \n' + str(total_hops))
print ('\nThe Key : \n' + str(key_response))
print ('\nThe Value : \n' + str(value_response))




clientSock.close()
print ('\nSocket Closed\n')
#   eof
