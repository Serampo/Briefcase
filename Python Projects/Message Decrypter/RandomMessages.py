import random

decryptext = str(random.randrange(1,99999999))

# We define the list of the alphabet for iteration purposes

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# We make a function that iterate trought the list to decrypt.

def decrypt(decryptext, alphabet):
    # Initialize an empty string to store the decrypted message
    plaintext = ""

    # Iterate through each character in the ciphertext
    for c in decryptext:
        # If the character is a number, substitute it using the alphabet
        if c.isdigit():
            index = int(c) - 1
            plaintext += alphabet[index]
        # If the character is not a number, leave it as is
        else:
            plaintext += c

    return plaintext

# Test the decrypt function

print(decrypt(decryptext, alphabet)) 
