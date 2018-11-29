#   Vic Chimenti
#   CPSC 5510 FQ18
#   p2 Distributed Hash Table
#   dht_client.py
#   created         11/26/2018
#   last modified   11/29/2018
#   Distributed Hash Table Client
#   /usr/local/python3/bin/python3




import socket           # for udp socket functionality
import sys              # for system calls
import argparse         # for parsing command line arguments




#   ***************     function definitions     ***************   #


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
def getIP(nd) :
    try :
        nd_ip = socket.gethostbyname(nd)
    except socket.gaierror :
        sys.stderr.write ("ERROR Invalid URL Entered : ")
        sys.exit ("Exiting Program")

    # convert host IP number to str for troubleshooting/testing
    node_ip_str = str(nd_ip)
    print ("node_ip_str : " + node_ip_str)
    if node_ip_str == MATCH_ALL :
            sys.stderr.write ("ERROR Invalid IP Number : ")
            sys.exit ("Exiting Program")

    return node_ip_str


#   ***************     end function definitions     ***************   #




# DEFINE CONTSANTS
MATCH_ALL = "0.0.0.0"                   # for IP validity checking

# parse and assign command-line input
parser = argparse.ArgumentParser()
parser.add_argument('node', type=str, nargs=1, default='cs1.seattleu.edu')
parser.add_argument('nodePort', type=int, nargs=1, default=10109)
parser.add_argument('operation', type=str, nargs=1)
parser.add_argument('key', type=str, nargs=1)
parser.add_argument('value', type=str, nargs='*', default='')
args = parser.parse_args()




# validate ip address
#ip_addr = getIP(str(args.node))

# connect to a node
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DRGAM)

# send key value pair
bytes_sent = clientSock.sendto(key, value, (str(args.node), int(args.nodePort)))
print ('sent {} bytes to {}'.format(bytes_sent, str(args.node)))

# receive response
response, response_node = sock.recvfrom(4096)
print ('received {} bytes from {}'.format(len(response), response_node))

clientSock.close()
print ('Socket Closed')
#   eof
