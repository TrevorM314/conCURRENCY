# Authors: Matthew Bouch and Trevor Mitchell

import hashlib
import time


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
    # Create the conCurrency blockchain
    conCurrency = BlockChain()

    # My local current version of the blockchain
    currentVersion = 0

    # Display the hash of the genesis block
    print(conCurrency.getLatestHash())

    # Create a new block on version 0
    conCurrency.createBlock(currentVersion, conCurrency.getLatestHash(), ["Trevor sent Bouch 5 conCurrency\n Bouch sent Trevor 2 conCurrency"], "Version 0 Block 1")

    # Display the hash of the new block
    print(conCurrency.getLatestHash())

    # Now lets update the blockchain to version 1
    conCurrency.updateVersion()

    # We will also update the version we are working on to version 1
    currentVersion = 1

    # Display the hash of the new block
    print(conCurrency.getLatestHash())

    # Create a new block on version 1
    conCurrency.createBlock(currentVersion, conCurrency.getLatestHash(), ["Bouch sent Joey 5 conCurrency\n Trevor sent Dr. Geisler 1000 conCurrency"], "Version 1 Block 1")

    #Create a new block on version 1
    conCurrency.createBlock(currentVersion, conCurrency.getLatestHash(), ["Joey sent Bouch 1 conCurrency\n Dr. Geisler sent Trevor 5 conCurrency"], "Version 1 Block 2")

    # Display the blockchain
    conCurrency.displayBlockChain()

main()