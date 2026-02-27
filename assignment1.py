
# Only alphabetic characters are shifted, others remain unchanged
import string

# user defined function for encryption
def caesar_encrypt(text, shift):
    result = ""
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    for ch in text:
        # for encrypting lowercase letters
        if ch.islower():
            result += lower[(lower.index(ch) + shift) % 26]
        
        # for encrypting upper letters

        elif ch.isupper():
            result += upper[(upper.index(ch) + shift) % 26]
       
    
         # for non alphabets chracter
        else:
            result += ch

     # for returning encrypted text
    return result

# user defined function for decryption

def caesar_decrypt(text, shift):
    result = ""
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    for ch in text:

        # decrypting lower case letters
        if ch.islower():
            result += lower[(lower.index(ch) - shift) % 26]

            # decrypting upper case letters
        elif ch.isupper():
            result += upper[(upper.index(ch) - shift) % 26]

            # decrypting non alphabetic chracters
        else:
            result += ch

    return result


# message which is going to be encrypted
message = "Ali lives in Pakistan. His age is 20. He studies at FAST University. Reg No: FA27-BSE-047"
# Shifting alphabets 6 places 
shift = 6

encrypted = caesar_encrypt(message, shift)
print("Encrypted Text:")
print(encrypted)

decrypted = caesar_decrypt(encrypted, shift)
print("\nDecrypted Text:")
print(decrypted)