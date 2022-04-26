# conCURRENCY protocol
**Authors:** Matthew Bouch and Trevor Mitchell\
**Version number:** 0

## Table of Contents
[1. Overview](#1-overview)\
[2. Protocol Updates](#2-protocol-updates)\
[3. Block Structure](#3-block-structure)\
[4. Transactions](#4-transactions)\
[5. Messages](#5-messages)

## 1. Overview
conCURRENCY is a blockchain protocol engineered toward preventing hard forks in the face of policy-chaning updates. It does so by preparing for a branch, in which the new protocol version is aware of the former protocol and accepts blocks that are mined on the proper branch.

## 2. Protocol Updates
At the core of the conCURRENCY protocol is the need for previous versions to payout when they want to future versions when they want, without double spending. Future versions of conCURRENCY *must* maintain a branched chain that follows the protocol of each previous version.

## 3. Block Structure
Blocks are limited to 100 kb each, and aim to be mined once every minute on average.

### 3.1 Header Fields
1. hash: 32 bytes\
    A sha-256 hash of the previous block on the blockchain
2. version: int, 4 bytes
3. time: int, 4 bytes\
    Time of creation of the block in seconds since unix epoch
4. nonce: int, 4 bytes\
    An arbitrary field used for proof of work
5. difficulty: int, 1 byte\
    The number of leading zeros required for the *next* hash to contain for the block to be accepted
6. miner: 32 bytes\
    The address of the miner's conCURRENCY account

### 3.2 Body
The body consists of transactions separated by a blank line. New lines are notated by the linefeed character, "\n".

## 4. Transactions

### 4.1 Inputs
A list of addresses used to supply the transaction with conCURRENCY. The transaction will take all of the available funds, so any remainder should be directed back to an address as an output. Any remaining conCURRENCY not attributed to an output address will be granted to the block miner as a reward.

### 4.2 Outputs
Each output contains both the address of the recipient and the amount of conCURRENCY being sent to the address.

Format:\
address: amount


## 5. Messages
All messages are sent over TCP/IP. All headers are encoded as ASCII characters. The body of messages may either be ASCII characters or raw data, depending on the type.\
The first line of a message contains the message type.\
The next line contains the version number header (e.g. "version: 0").\
The following lines contain any other headers needed for the given message type\
After all the headers, the next line is empty, followed by the start of the message body.

### 5.1 GET_PEERS
When the sender sends this message to a conCURRENCY node, the receiving node should respond with a list of ip addresses that correspond to its peers on the conCURRENCY network.

**body**: a list of IPv4 addresses in dot-decimal notation separated by a newline character, "\n." For example, 192.0.2.12.\
body encoding: ASCII

### 5.2 PEERS
A node should send this in response to a GET_PEERS message to the requesting node. This message contains a list of IP addresses of known conCURRENCY nodes.

**body:** the list of IPv4 addresses separated by a newline character.\
body encoding: ASCII

### 5.3 PUT_BLOCK
When a node receives an PUT_BLOCK message with a block that follows all protocol rules, and points to the previously most recent block, the receiving node should update its cached chain and forward the PUT_BLOCK message to all other neighbors

If the new block does not point to the most recent block, or if it violates any rules, the receiver should disregard the message.

**body:** a legal block containing all of the necessary information.\
body encoding: Raw binary (should be parsed using the rules of the block structure)

### 5.4 PUT_TRANSACTION
When a user wishes to add a transaction to the mempool, they send a PUT_TRANSACTION message to all neighbors.

This transaction must contain valid addresses and proper authorization (including secret key signing).

When a node receives a PUT_TRANSACTION message that is not currently in its local mempool, the node should store that transaction and send the PUT_TRANSACTION to all other neighbors.

**Body:** A legal conCURRENCY transaction\
Body encoding: ASCII

### 5.5 GET_CHAIN
When a node hopes to start out and get the blockchain, it sends this message to its neighbors to obtain it. The node should send this message to multiple neighbors in order to validate the chain.

### 5.5 CHAIN
This message is sent in response to the GET_CHAIN message. It contains a list of all blocks on the chain.