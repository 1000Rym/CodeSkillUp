"""
Multi-threading socket programming - Server.

Args: 
    address: server's address
    port: server's port
    blacklog: backlog(Limit counts of the clients that the server accpet)
"""

import sys
import socket
from _thread import *
# import threading

HOST = '127.0.0.1'
PORT = 65432
BLACKLOG = 10

# A lock object used to change lock states(lock and unlock) of the thread.
# print_lock.acquire() :change state to lock.
# print_lock.release() :change state to unlock.
# print_lock = threading.Lock()

def print_and_return_recv_msg(conn,addr):
    """ 
    Print and Return the message that the connection received.

    Args:
        conn: connection between client and server.
        addr: address info via server to client.
        
    Return: Return false when the program finished.
    """
    while True:
        data = conn.recv(1024)
        
        if not data: 
            print(f'Disconnect Connection to {addr[0]}:{addr[1]}')
            #print_lock.release()
            break
        
        print(f"You have received msg from {addr[0]}:{addr[1]}->{data.decode()}")
        conn.send(data)
    
    conn.close()      
    

def run_tcp_multi_connect_server(address = HOST, port = PORT, blacklog = BLACKLOG):
    """
    Run the TCP multi-connecting servers.

    Args:
        address (str, optional): The server's IP Address Defaults to HOST.
        port (int, optional): The server's port number. Defaults to PORT.
        blacklog (int, optional): The limit counts that client could access. Defaults to BLACKLOG.
    """ 
    # AF_INET : IPV4 connections.
    # SOCK_STREAM : TCP connection. 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((address, port))
        s.listen(blacklog)
        
        print(f"Run Server Address:{address}:{port}, Black Log:{blacklog}")
        
        while True:
            conn, addr = s.accept()
            
            # Lock the states 
            # print_lock.acquire()
            print(f"New client {addr[0]}:{addr[1]} is connected.")
            start_new_thread(print_and_return_recv_msg, (conn, addr))
           

if __name__ == '__main__':
    address = HOST if len(sys.argv)<2 else sys.argv[1]
    port = PORT if len(sys.argv)<3 else sys.argv[2]
    blacklog = BLACKLOG if len(sys.argv)<4 else sys.argv[3]
    run_tcp_multi_connect_server(address, port, blacklog)

