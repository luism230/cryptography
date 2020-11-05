import string
import random
import math

def get_vKey(key, mlength):
    newkey = ''
    while len(newkey) < mlength:
        for i in key:
            if len(newkey) < mlength:
                newkey += i
    return newkey 

# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    end = ord('Z')
    start = ord('A') - 1

    if offset > 26:
        offset = offset%26

    newText = ''
    for i in plaintext:
        value = ord(i)

        if value > end or value < start + 1:
            newText += chr(value)
        elif value + offset > end:
            new_offset = offset - (end - value)
            newText += chr(start + new_offset)
        else:
            newText += chr(value + offset)
    return newText
# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    end = ord('Z') + 1
    start = ord('A')

    if offset > 26:
        offset = offset%26

    original = ''
    for i in ciphertext:
        value = ord(i)
        if value > end - 1 or value < start:
            original += chr(value)
        elif value - offset < start:
            new_offset = offset - (value - start)
            original += chr(end - new_offset)
        else:
            original += chr(value - offset)
    return original

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    keyword = get_vKey(keyword, len(plaintext))
    alphabet = list(string.ascii_uppercase)
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
    keyword = get_vKey(keyword, len(ciphertext))
    alphabet = list(string.ascii_uppercase)
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
    w = [1]

    count = 1
    total = w[0]
    while count < n:
        new = random.randint(total+1, 2*total)
        w.append(new)
        total += new
        count+=1
    W = tuple(w)
    Q = random.randint(total+1, 2*total)

    R = random.randint(2, Q-1)
    while math.gcd(Q, R) != 1:
        R = random.randint(2, Q-1)
    return (W, Q, R)


# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    W = private_key[0]
    Q = private_key[1]
    R = private_key[2]

    B = []
    for i in W:
        B.append((R*i)%Q)
    B = tuple(B)

    return B

def bytes_to_bits(byte):
    bits = []
    for i in byte:
        bit = bin(i)
        bit = bit.replace('b', '')
        while len(bit) < 8:
            bit = '0' + bit
        bits.append(bit) 
    return bits

def bits_to_bytes(bit):
    byte = []
    for i in bit:
        byte.append(int(i,2))
    message = ''
    for i in byte:
        message += chr(i)
    return message

# Arguments: string, tuple (W, Q, R)
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    byte = []
    for i in plaintext:
        byte.append(ord(i))
    bits = bytes_to_bits(byte)
    encrypted = []
    for i in bits:
        C = 0
        for j in range(0,8):
            C += int(i[j]) * public_key[j]

        encrypted.append(C)
    return encrypted



# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    W = private_key[0]
    Q = private_key[1]
    R = private_key[2]
    S = 1
    while (R*S)%Q != 1:
        S+=1

    cPrime = []
    for i in ciphertext:
        cPrime.append((i*S)%Q)
    
    
    decrypted = []
    for i in cPrime:
        m = ''
        for j in reversed(W):
            if i >= j:
                m = '1' + m 
                i = i - j
            else:
                m = '0' + m
        decrypted.append(m)

    return bits_to_bytes(decrypted)


def main():
    # Testing code here
    pass

if __name__ == "__main__":
    main()


