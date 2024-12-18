# Tables and necessary parameters
INITIAL_PERMUTATION = [58, 50, 42, 34, 26, 18, 10, 2,
                       60, 52, 44, 36, 28, 20, 12, 4,
                       62, 54, 46, 38, 30, 22, 14, 6,
                       64, 56, 48, 40, 32, 24, 16, 8,
                       57, 49, 41, 33, 25, 17, 9, 1,
                       59, 51, 43, 35, 27, 19, 11, 3,
                       61, 53, 45, 37, 29, 21, 13, 5,
                       63, 55, 47, 39, 31, 23, 15, 7]

FINAL_PERMUTATION = [40, 8, 48, 16, 56, 24, 64, 32,
                     39, 7, 47, 15, 55, 23, 63, 31,
                     38, 6, 46, 14, 54, 22, 62, 30,
                     37, 5, 45, 13, 53, 21, 61, 29,
                     36, 4, 44, 12, 52, 20, 60, 28,
                     35, 3, 43, 11, 51, 19, 59, 27,
                     34, 2, 42, 10, 50, 18, 58, 26,
                     33, 1, 41, 9, 49, 17, 57, 25]

PC1 = [57, 49, 41, 33, 25, 17, 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27,
       19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29,
       21, 13, 5, 28, 20, 12, 4]

PC2 = [14, 17, 11, 24, 1, 5,
       3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8,
       16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48,
       44, 49, 39, 56, 34, 53,
       46, 42, 50, 36, 29, 32]

SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2,
                  1, 2, 2, 2, 2, 2, 2, 1]

# Function to apply a permutation
def permute(block, table):
    # Adjust the block length to ensure it's sufficient
    return ''.join(block[i - 1] for i in table)

# Function to convert text to binary
def text_to_bin(text):
    return ''.join(format(ord(c), '08b') for c in text)

# Function to convert binary to text
def bin_to_text(binary):
    chars = [binary[i:i + 8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(c, 2)) for c in chars)

# Function to split a block into two parts
def split_block(block):
    mid = len(block) // 2
    return block[:mid], block[mid:]

# Function to perform a circular left shift
def circular_left_shift(bits, shifts):
    return bits[shifts:] + bits[:shifts]

# Function to generate the 16 subkeys
def generate_subkeys(key):
    key_bin = text_to_bin(key)
    permuted_key = permute(key_bin, PC1)
    left, right = split_block(permuted_key)
    subkeys = []
    for shifts in SHIFT_SCHEDULE:
        left = circular_left_shift(left, shifts)
        right = circular_left_shift(right, shifts)
        combined = left + right
        subkeys.append(permute(combined, PC2))
    return subkeys

# Function to perform DES encryption
def des_encrypt(block, subkeys):
    block = permute(block, INITIAL_PERMUTATION)  # Apply the initial permutation
    left, right = split_block(block)
    
    for subkey in subkeys:
        expanded_right = permute(right, [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])  # Expand the right half
        xor_result = ''.join(str(int(a) ^ int(b)) for a, b in zip(expanded_right, subkey))  # XOR with the subkey
        left, right = right, ''.join(str(int(a) ^ int(b)) for a, b in zip(left, xor_result))  # Swap left and right
    combined = right + left  # Combine the left and right parts
    return permute(combined, FINAL_PERMUTATION)  # Apply the final permutation

# Function to perform DES decryption
def des_decrypt(block, subkeys):
    block = permute(block, INITIAL_PERMUTATION)  # Apply the initial permutation
    left, right = split_block(block)

    # Perform decryption steps by reversing the subkeys
    for subkey in reversed(subkeys):
        expanded_right = permute(right, [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])
        xor_result = ''.join(str(int(a) ^ int(b)) for a, b in zip(expanded_right, subkey))
        left, right = right, ''.join(str(int(a) ^ int(b)) for a, b in zip(left, xor_result))
    combined = right + left
    return permute(combined, FINAL_PERMUTATION)

# Interactive program for DES encryption/decryption
def interactive_des():
    print("=== DES Encryption/Decryption ===")
    choice = input("Do you want to encrypt or decrypt? (Enter 'encrypt' or 'decrypt'): ").strip().lower()

    if choice not in ['encrypt', 'decrypt']:
        print("Invalid choice!")
        return

    text = input("Enter the text (8 characters): ")
    key = input("Enter the key (8 characters): ")

    if len(text) != 8 or len(key) != 8:
        print("Error: The text and the key must be exactly 8 characters.")
        return

    # Convert to binary
    binary_text = text_to_bin(text)
    subkeys = generate_subkeys(key)

    if choice == 'encrypt':
        # Encryption
        encrypted_bin = des_encrypt(binary_text, subkeys)
        encrypted_text = bin_to_text(encrypted_bin)
        print(f"Encrypted text: {encrypted_text}")
    elif choice == 'decrypt':
        # Decryption
        decrypted_bin = des_decrypt(binary_text, subkeys)
        decrypted_text = bin_to_text(decrypted_bin)
        print(f"Decrypted text: {decrypted_text}")

# Run the interactive DES program
interactive_des()
