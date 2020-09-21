# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    newText = ''
    for i in plaintext:
        newText += chr(ord(i) + offset)
    print(newText)
    return newText

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    original = ''
    for i in ciphertext:
        original += chr(ord(i) - 1)
    print(original)

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    pass

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    pass

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    pass

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    pass

# Arguments: string, tuple (W, Q, R)
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    pass

# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    pass

def main():
    # Testing code here
    word = input("Enter Input to encrypt\n")
    number = int(input("Enter number to offset\n"))
    encyrpted_word = encrypt_caesar(word, number)
    decrypt_caesar(encyrpted_word, number)
        

if __name__ == "__main__":
    main()

    

