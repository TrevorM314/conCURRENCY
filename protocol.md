# conCURRENCY protocol
**Authors:** Matthew Bouch and Trevor Mitchell\
**Version number:** 0

## Table of Contents
[1. Overview](#1-overview)\
[2. Protocol Updates](#2-protocol-updates)\
[3. Block Structure](#3-block-structure)\
[4. Messages](#4-messages)

## 1. Overview
conCURRENCY is a blockchain protocol engineered toward preventing hard forks in the face of policy-chaning updates. It does so by preparing for a branch, in which the new protocol version is aware of the former protocol and accepts blocks that are mined on the proper branch.

## 2. Protocol Updates
At the core of the conCURRENCY protocol is the need for previous versions to payout when they want to future versions when they want, without double spending. Future versions of conCURRENCY *must* maintain a branched chain that follows the protocol of each previous version.

## 3. Block Structure
Blocks are limited to 100 kb each, and aim to be mined once every minute on average.

### 3.1 Header Fields
1. hash: string, 32 bytes\
    A sha-256 hash of the previous block on the blockchain
2. version: int, 4 bytes
3. time: int, 4 bytes\
    Time of creation of the block in seconds since unix epoch
4. nonce: int, 4 bytes\
    An arbitrary field used for proof of work
5. difficulty: int, 1 byte\
    The number of leading zeros required for the *next* hash to contain for the block to be accepted

### 3.2 Body
The body consists of transactions separated by a blank line. New lines are notated by the linefeed character, "\n".

## 4. Transactions

## 5. Messages
All messages are sent over TCP/IP.

### 5.1 GET_PEERS
When the sender sends this message to a conCURRENCY node, the receiving node should respond with a list of ip addresses that correspond to its peers on the conCURRENCY network.

### 5.2 PEERS
The response to GET_PEERS containing the list of IP addresses.

### 5.3 UPDATE_CHAIN
When a node receives an UPDATE_CHAIN message with a chain that follows all protocol rules, and is longer than the chain that the node is currently working with, the node should adopt the new chain and forward it on to all other neighbors with an UPDATE_CHAIN message.

If the chain is not longer than the node's current chain, or it violates any rules, the receiver should disregard the message.

### 5.4 PUT_TRANSACTION
When a user wishes to add a transaction to the mempool, they send a PUT_TRANSACTION message to all neighbors.

This transaction must contain valid addresses and proper authorization (including secret key signing).

When a node receives a PUT_TRANSACTION message that is not currently in its local mempool, the node should store that transaction and send the PUT_TRANSACTION to all other neighbors.