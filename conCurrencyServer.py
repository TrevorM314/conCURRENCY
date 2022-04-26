# Authors: Matthew Bouch and Trevor Mitchell
# Guide Link: https://medium.com/codex/make-a-client-talk-to-a-local-server-with-python-socket-programming-1-9be3cb4b474

import hashlib
import time
import socket
import sys


class BlockChain:
    blockChain = [[]]
    version = 0
    def __init__(self):
        self.blockChain = [[]]
        self.createBlock(self.version, "Genesis", [], "Genesis")
    
    def createBlock(self, version, previousHash, transactions, blockName):
        self.blockChain[version].append(block(previousHash, transactions, blockName, version))

    def getLatestHash(self):
        return self.blockChain[self.version][-1].blockHash

    def updateVersion(self):
        self.blockChain.append([])
        self.createBlock(self.version+1, self.getLatestHash(), [], ("Version " + str(self.version+1) + " Update"))
        self.version += 1
    
    def displayBlockChain(self):
        printList = []
        for i in range(len(self.blockChain)):
            printList.append([])
            for j in range(len(self.blockChain[i])):
                printList[i].append(self.blockChain[i][j].blockName)
        print(printList)


class block:
    previousHash = ""
    transactions = ""
    blockHash = None
    version = 0
    nonce = 0
    difficulity = 0
    miner_address = "0"
    time_of_creation = None
    blockName = ""
    def __init__(self, previousHash, transactions, blockName, version):
        # add all strings in list transactions to a string
        self.previousHash = previousHash
        self.transactions = transactions
        self.blockHash = self.calculateHash()
        self.blockName = blockName
        self.version = version
        self.nonce = 0
        self.difficulity = 0
        self.miner_address = "0"
        self.time_of_creation = time.time()

    def calculateHash(self):
        # add all strings in list transactions to a string
        blockString = self.previousHash + str(self.transactions)
        # hash the string
        blockHash = hashlib.sha256(blockString.encode()).hexdigest()
        return blockHash


def main():
    # Create a TCP/IP socket
    sock = socket.socket()

    # Set a port for the socket
    port = 5001

    # Bind the socket to the port
    sock.bind(('', port))

    # Listen for incoming connections
    sock.listen(5)

    print("server is listening on port: " + str(port))

    # Create the conCurrency blockchain
    conCurrency = BlockChain()

    while True:
        # Wait for a connection
        connection, addr = sock.accept()

        # Send a hello message to the client
        message = "Hello Client"
        connection.send(message.encode("utf-8"))

        # Now wait for the client to send a message to us about a block
        data = connection.recv(1024)
        data = data.decode("utf-8")
        data = data.split(",")
        print(data)

        conCurrency.createBlock(int(data[0]), conCurrency.getLatestHash(), data[1], ("Version " + str(int(data[0])) + " Block 1"))

        # Shut down the connection
        print("Shutting Down!")
        connection.close()
        break

    conCurrency.displayBlockChain()


main()