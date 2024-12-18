# DES Implementation in Python

This repository contains a Python implementation of the DES (Data Encryption Standard) cryptographic algorithm. It includes functions for:

- Encrypting messages using the DES algorithm.
- Decrypting messages using the DES algorithm.
- A demo of usage with example outputs.

## Overview

DES (Data Encryption Standard) is a symmetric-key algorithm used for the encryption of data. Although it is now considered insecure for many applications, DES was widely used for secure data transmission in the past. The implementation in this repository follows the basic principles of DES encryption, including:

- **Encryption**: Encrypts data using a secret key.
- **Decryption**: Decrypts encrypted data using the same secret key.

## Features

- **Encryption**: The message is encrypted by dividing it into 64-bit blocks, performing multiple rounds of substitution and permutation using a 56-bit key.
- **Decryption**: The encrypted message is decrypted using the same key by reversing the encryption steps.
  
### Key Generation

- DES uses a 56-bit key for encryption, which is expanded into 16 subkeys for each round of the algorithm.

### Encryption and Decryption

- **Encryption**: The message is divided into 64-bit blocks and encrypted using the DES algorithm with the public key.
- **Decryption**: The encrypted message is decrypted using the same key in reverse order.

## How to Run

1. Clone this repository to your local machine.
2. Install the required dependencies (if applicable).
3. Run the `des_encryption.py` file to test encryption and decryption.

Example usage:

```bash
python des_encryption.py
