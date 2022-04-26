# Authors: Matthew Bouch and Trevor Mitchell
# Guide Link: https://medium.com/codex/make-a-client-talk-to-a-local-server-with-python-socket-programming-1-9be3cb4b474

import socket
import sys

def main():
    # Create a TCP/IP socket
    sock = socket.socket()

    # Set a port for the socket
    port = 5001

    # Connect the socket to the port
    sock.connect(('localhost', port))

    # My local current version of the blockchain
    currentVersion = 0

    # Receives the message from the server
    message = sock.recv(1024)
    message = message.decode("utf-8")
    print(message)

    # Send a message to the server
    message = str(currentVersion) + "," + "Trevor sent Bouch 5 conCurrency\n Bouch sent Trevor 2 conCurrency"
    sock.send(message.encode("utf-8"))

    sock.close()

main()