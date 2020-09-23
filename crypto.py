import string
# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    newText = ''
    for i in plaintext:
        newText += chr(ord(i) + offset)
    print(newText)
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

def get_encryption_method():
    method = input("Enter 'c' for Caeser Cypher\nEnter 'v' for Vignere\nor Enter 'm' for MHK Cryptosystem\n")
    method = method.lower()
    while method != 'c' and method != 'v' and method != 'm':
        print('Incorrect Input. Try again')
        encryption_method = input("Enter 'c' for Caeser Cypher\nEnter 'v' for Vignere\nor Enter 'm' for MHK Cryptosystem\n")
    return method

def get_message():
    word = input("Enter Input to encrypt (No non-alphabetical characters)\n")
     #Prevent user from inputting non-alphabetical character
    while len(word) < 1:
        print("Input must be at least one character long")
        word = input("Enter Input to encrypt (No non-alphabetical characters)\n")

    wrong = False
    for i in word:
        if i not in string.ascii_lowercase:
            wrong = True

    while wrong:
        wrong = False
        print("Incorrect Input. No non-alphabetical characters allowed")
        word = input("Enter Input to encrypt (No non-alphabetical characters)\n")
        for i in word:
            if i not in string.ascii_lowercase:
                wrong = True
    return word


def main():
    # Testing code here
    
    #  Will only accept 'e' or 'd' as an option
    answer = input("Enter 'e' to Encrypt\nEnter 'd' to Decrypt\n")
    while answer.lower() != 'e' and answer != 'd':
        print('Incorrect Input. Try again')
        answer = input("Enter 'e' to Encrypt\nEnter 'd' to Decrypt\n")
    if answer == 'e':
        
        # Prevents wrong inputs
        encryption_method = get_encryption_method()
        if encryption_method.lower() == 'c':
            message = get_message()


            number = int(input("Enter number to offset\n"))
            while type(numeber) is not int:
                print("Incorrect Input. Please only use numbers")
                number = int(input("Enter number to offset\n"))

            encrypt_caesar(message, number)

        elif encryption_method.lower() == 'v':
            pass
        else:
            pass
    else:

        # Prevents wrong inputs
        decryption_method = input("Enter 'c' for Caeser Cypher\nEnter 'v' for Vignere\nor Enter 'm' for MHK Cryptosystem\n")
        while decryption_method.lower() != 'c' and decryption_method != 'v' and decryption_method != 'm':
            print('Incorrect Input. Try again')
            decryption_method = input("Enter 'c' for Caeser Cypher\nEnter 'v' for Vignere\nor Enter 'm' for MHK Cryptosystem\n")
        if decryption_method.lower() == 'c':
            word = input("Enter Input to encrypt\n")
            number = int(input("Enter number to offset\n"))
            decrypt_caesar(word, number)
        elif decryption_method.lower() == 'v':
            pass
        else:
            pass
    

        

if __name__ == "__main__":
    main()

    


