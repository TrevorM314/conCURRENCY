# conCURRENCY protocol
**Authors:** Matthew Bouch and Trevor Mitchell\
**Version number:** 0.0

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

## 4. Messages