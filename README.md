Cryptographic Algorithm Implementation: DES (Data Encryption Standard)

Overview

This project implements the DES (Data Encryption Standard) block cipher in Python. DES is a symmetric-key algorithm used for data encryption. It operates on 64-bit blocks of data and uses a 56-bit key for encryption and decryption. The project includes both encryption and decryption processes, demonstrating how DES works under the hood.

This implementation has been simplified for educational purposes while still demonstrating the core concepts of the DES algorithm, including permutation, expansion, substitution, and XOR operations.

Features

DES Block Cipher: Implementation of both encryption and decryption processes.
Key Scheduling: Generates 16 sub-keys from the main key using PC1, PC2, and circular left shifts.
Permutation and Expansion: Uses Initial and Final Permutation tables, along with an expansion of the right half during the rounds.
Interactive Mode: A simple interactive user interface where you can encrypt and decrypt text of your choice.
Prerequisites

Python 3.x
Basic understanding of cryptography and block ciphers.
How to Run

Clone the repository:
git clone https://github.com/yourusername/des-cryptography.git
Navigate to the project directory:
cd des-cryptography
Run the des.py file to start the interactive mode:
python des.py
The program will prompt you to choose whether you want to encrypt or decrypt a message. Enter your desired text (8 characters) and key (8 characters) when prompted.
Code Explanation

Key Steps
Permutation: The input text and keys go through several permutations (Initial and Final Permutation), which shuffle bits according to predefined tables.
Key Generation: The original key goes through the PC1 and PC2 steps to generate 16 subkeys used in the 16 rounds of the DES algorithm.
Rounds: In each round, the right half of the text is expanded and XORed with the subkey. The result is passed through a substitution box (S-box) and combined with the left half to form the new text.
XOR Operations: At the heart of the DES algorithm, XOR is used for combining the input with the subkeys.
Functions Implemented
permute: Applies a permutation to a block of data using a given permutation table.
text_to_bin: Converts a string into its binary representation.
bin_to_text: Converts a binary string back to text.
split_block: Splits a block of data into two halves.
circular_left_shift: Performs a left shift operation on the bits.
generate_subkeys: Generates 16 subkeys used in the DES encryption process.
des_encrypt: Performs the DES encryption algorithm on a given block using the subkeys.
des_decrypt: Performs the DES decryption algorithm, reversing the encryption process.
