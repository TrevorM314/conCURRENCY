# Authors: Matthew Bouch and Trevor Mitchell
# Guide Link: https://medium.com/codex/make-a-client-talk-to-a-local-server-with-python-socket-programming-1-9be3cb4b474

import hashlib
import time
import socket
import sys

from pyparsing import And


class BlockChain:
    blockChain = [[]]
    version = 0
    def __init__(self):
        self.blockChain = [[]]
        self.createBlock(self.version, "Genesis", [], "Genesis")
        self.difficulty = ((2**256) / 2)
    
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

    def isNewBlockValid(self, newBlock):
        tmp1 = int(newBlock.blockHash, base=16)
        tmp2 = self.difficulty
        if tmp1 <= tmp2:
            return True
        else:
            return False

# Will want a length field along with a data field
# This will be so the translation into bytes can be known with how many bytes are a part of each block.
# Use a VarInt to encode the length of the data field
# Find out how Bitcoin or Ethereum does this to match them.

# How to mine a block
# Difficulty is how many zeros need to be in the front of the hash
    # Changing this difficulty makes something twice as easy or twice as hard.
    # But we don't want this so heres how to get around it.
# n#0s -> <= 2^(256-2)
# x <= 2^(256-2) -> d(n)
# X <= d(n)
# d(n+1) = d(n) * delta
# delta for bitcoin = (time for last 2016 blocks) / (2016 * 10 minutes)
# straight up less then or equal against the difficulty level.
# To mine this and do the rehashing you use the nonce and edit that to find the proper value to be less then the difficulty level.

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
    def __init__(self, previousHash, transactions, blockName, version, nonce=0):
        # add all strings in list transactions to a string
        self.previousHash = previousHash
        self.transactions = transactions
        self.blockName = blockName
        self.version = version
        self.nonce = nonce
        self.difficulity = 0
        self.miner_address = "0"
        self.time_of_creation = time.time()
        self.blockHash = self.calculateHash()

    def calculateHash(self):
        # add all strings in list transactions to a string
        blockString = self.previousHash + str(self.transactions) + str(self.nonce)
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

        hashVal1 = int(conCurrency.getLatestHash(), base=16)
        print("Hash Val 1: " + str(hashVal1))

        conCurrency.createBlock(int(data[0]), conCurrency.getLatestHash(), data[1], ("Version " + str(int(data[0])) + " Block 1"))

        hashVal2 = int(conCurrency.getLatestHash(), base=16)
        print("Hash Val 2: " + str(hashVal2))


        # Shut down the connection
        print("Shutting Down!")
        connection.close()
        break

    
    # We can now try to mine a block
    # We can mine a block by finding a hash that is less then the difficulty level
    #! previousHash, transactions, blockName, version, nonce=0
    result = False
    transactions = "I pay Dr. Geisler 5 conCurrency"
    versionStr = "Version " + str(int(conCurrency.version))
    nonce = 0
    while result == False and nonce < 10:
        myBlock = block(conCurrency.getLatestHash(), transactions, versionStr, conCurrency.version, nonce)
        print("Nonce: " + str(nonce))
        print("My Block's Value: " + str(int(myBlock.blockHash, base=16)))
        print("Current Difficulty: " + str(conCurrency.difficulty))
        result = conCurrency.isNewBlockValid(myBlock)
        if result == False:
            nonce += 1
        print("Result: " +  str(result))

    conCurrency.displayBlockChain()


main()