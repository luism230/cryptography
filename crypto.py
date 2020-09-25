import string
# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    end = ord('z')
    start = ord('a') - 1

    while offset > end:
        offset -= end

    newText = ''
    for i in plaintext:
        value = ord(i)
        if value + offset > end:
            new_offset = offset - (end - value)
            newText += chr(start + new_offset)
        else:
            newText += chr(ord(i) + offset)
    return newText
# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    end = ord('z') + 1
    start = ord('a')

    while offset > end -1:
        offset -= end -1

    original = ''
    for i in ciphertext:
        value = ord(i)
        if value - offset < start:
            new_offset = offset - (value - start)
            original += chr(end - new_offset)
        else:
            original += chr(ord(i) - 1)
    return original

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    alphabet = list(string.ascii_lowercase)
    end = ord('z')
    start = ord('a') - 1
    newText = ''

    count = 0
    while len(newText) < len(plaintext):
        offset = alphabet.index(keyword[count])
        newText += encrypt_caesar(plaintext[count], offset)
        count+= 1
    return newText


# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    alphabet = list(string.ascii_lowercase)
    count = 0
    newText = ''

    while len(newText) < len(ciphertext):
        offset = alphabet.index(keyword[count])
        newText += decrypt_caesar(ciphertext[count], offset)
        count+= 1
    return newText


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
    word = input("Enter Input (No non-alphabetical characters)\n")
     #Prevent user from inputting non-alphabetical character
    while len(word) < 1:
        print("Input must be at least one character long")
        word = input("Enter Input (No non-alphabetical characters)\n")

    wrong = False
    for i in word:
        if i not in string.ascii_lowercase:
            wrong = True

    while wrong:
        wrong = False
        print("Incorrect Input. No non-alphabetical characters allowed")
        word = input("Enter Input (No non-alphabetical characters)\n")
        for i in word:
            if i not in string.ascii_lowercase:
                wrong = True
    return word

def get_num():
    number = input("Enter Offset Number\n")
    while number.isnumeric() == False:
        print("Incorrect Input. Please only use numbers")
        number = input("Enter number to offset\n")
    return int(number)


def get_vKey(message):
    print('Enter Key')
    key = get_message()
    newkey = ''
    while len(newkey) < len(message):
        for i in key:
            if len(newkey) < len(message):
                newkey += i.lower()
    return newkey


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
            number = get_num()

            print(encrypt_caesar(message, number))

        elif encryption_method.lower() == 'v':
            message = get_message()

            key = get_vKey(message)
            print(encrypt_vigenere(message, key))
        else:
            pass
    else:

        # Prevents wrong inputs
        decryption_method = get_encryption_method()
        if decryption_method.lower() == 'c':
            message = get_message()
            number = get_num()
            print(decrypt_caesar(message, number))
        elif decryption_method.lower() == 'v':
            message = get_message()
            key = get_vKey(message)
            print(decrypt_vigenere(message, key))
        else:
            pass
    

        

if __name__ == "__main__":
    main()

    


