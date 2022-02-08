"""
Simple TCP client program used for establishing
connection with TCP Client.
arguments: 
- address : IP address Info.
- port number : IP port Info.
"""
import sys
import socket

HOST = '127.0.0.1'
PORT = 65432

def run_tcp_server(address = HOST, port = PORT):
    """ 
    Run the TCP server.
    arg1: IP address
    arg2: port number
    """
    
    print("address=", address,", port=", port)
    
    # AF_INET stands for IPV4 connection.
    # SOCK_STREAM stands for the TCP connection.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((address, port))
        s.listen()
        
        conn, addr = s.accept()
        with conn: 
            print('Connected by ', addr[0],":",addr[1])
            while True:
                # Maximum data received at once is 1024 bytes.
                data = conn.recv(1024) 
                if not data:
                    break
                conn.sendall(data)
    

if __name__ == '__main__': 
    address = HOST if len(sys.argv)<2 else sys.argv[1]
    port = PORT if len(sys.argv)<3 else sys.argv[2]
    run_tcp_server(address, int(port))
