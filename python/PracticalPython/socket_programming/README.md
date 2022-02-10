# Socket Programming In Python
This page is made for understanding main functions and methods in Python's [socket module](https://docs.python.org/3/library/socket.html).

## Primary Socket API
Python's socket module provides the following modules.
- `socket()` : returns socket object whose methods implement the various socket system calls.
- `bind(address)` : bind the socket to the __address__.
- `listen([backlog])`: enable a server to accept connection.
- `accept()`: accept a connection. The socket must be bound to an address and listning for connections.
- `connect()`: connect a remote address.
- `connect_ex()`: like `connect()`, but return an error indicator instead of rasising an exception.
- `send(bytes)`: send data to the socket.
- `recv(bufsize)`: recive data from the socket.
- `close()`: market socket closed.

## TCP Socket Flow(Single Thread Socket Programming)
Here is the diagram indicates the sequence of socket API calls and data flow for the TCP connection(Sockets TCP Flow).
![Sockets TCP Flow](figure/sockets_tcp_flow.png)
- Server side code:  [tcp_server.py](tcp_server.py) 
- Client side code: [tcp_client.py](tcp_client.py)

## Socket Programming with Multi-threading in Python
Executing multiple threads simultaneously in a single process. Following modules are supported to handle multi-threading.
- Modules for support multi-thread
    - [_thread](https://docs.python.org/ko/3/library/_thread.html): low-level primitives for working with multiple threads.
    - [threading](https://docs.python.org/ko/3/library/threading.html): higher-level interfaces on top of `_thread`. 
- Multi-Thread server side code: [tcp_server_multi.py](tcp_server_multi.py)
- Multi-Thread client side code: [tcp_client_msg.py](tcp_client_msg.py)

## Other Tip
- How to release the port that have been used.
    ```shell
    $ lsof -i -n | grep port_number
    ```

## Reference
- [Real Python: Socket Programming in Python](https://realpython.com/python-sockets/)
- [Geeks for Geeks: Socket Programming with Multi-threading in Python](https://www.geeksforgeeks.org/socket-programming-multi-threading-python/)