"""
Simple TCP client program used for establishing
connection with TCP server.
arguments: 
- address : Target server's IP address Info.
- port number : Target server's port Info.
"""
import sys
import socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 65432

def connect_tcp_server(server_addr = SERVER_ADDRESS, server_port = SERVER_PORT):
    """ 
    Run the TCP server.
    arg1: IP address
    arg2: port number
    """
    
    print("server address=", server_addr,", server port=", server_port)
    
    # AF_INET stands for IPV4 connection.
    # SOCK_STREAM stands for the TCP connection.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_addr, server_port))
       
        while True:
            msg = input("Send the message:")
            if msg == 'end':
                break
            
            s.send(msg.encode())
            data = s.recv(1024)
            print('Recieve message from server:', repr(data.decode()))           
        
        # close socket connection.
        s.close()
    

if __name__ == '__main__': 
    address = SERVER_ADDRESS if len(sys.argv)<2 else sys.argv[1]
    port = SERVER_PORT if len(sys.argv)<3 else sys.argv[2]
    connect_tcp_server(address, int(port))
