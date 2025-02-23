import string

# GOAL:
# decode the given ciphertext by finding the key

ciphertext_hex = "4d5f595f525b595149594e5c41425548655349655c4f5447" #given cipher text
ciphertext = bytes.fromhex(ciphertext_hex) #converts hex to bytes

# HINT: 
# helpful function!
#       If the byte array contains invalid sequences that 
#       cannot be decoded with UTF-8, a UnicodeDecodeError is raised. 
def is_printable_ascii(byte_array):
    try:
        message = byte_array.decode('utf-8') # decodes byte array to string using UTF-8 encoding
            # string.printable is a predefined set of characters
        return all(c in string.printable for c in message) # True if all characters in message are in string.printable
    except UnicodeDecodeError:
        return False