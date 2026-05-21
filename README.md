# Secure File Transfer Challenge

## Overview
This project securely encrypts, transfers, and decrypts files using Python.

## Features
- AES-based Fernet encryption
- TCP/IP socket transfer
- Secure decryption

## Technologies Used
- Python
- Socket Programming
- Cryptography Library

## Setup

Install dependency:

pip install cryptography

Run:

python generate_key.py

python encrypt.py

python server.py

python client.py

python decrypt.py

## Workflow

Sender:
Original File → Encryption → Transfer

Receiver:
Receive File → Decryption → Original File