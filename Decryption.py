p = int(input("Prime number: "))
private_key = int(input("Private key: "))
ciphertext = eval(input("Ciphertext (list of pairs): "))

def decrypt_message(private_key, ciphertext, p):
    decrypted_message = ""  # empty string to store the decrypted message
    for c1, c2 in ciphertext:  # Loop through each pair (c1, c2)
        s = pow(c1, private_key, p)    # Decrypt c1 using the private key, s = (c1^x) mod p  
        s_inverse = pow(s, -1, p)         # Compute the modular inverse of the shared secret: s_inverse = s^(-1) mod p
        message_int = (c2 * s_inverse) % p   # Decrypt the original message integer using the formula: m = (c2 * s_inverse) mod p
        decrypted_message += chr(message_int) # Convert the decrypted integer back to its character representation

    return decrypted_message  #return the decrypted message as a string 

decrypted_message = decrypt_message(private_key, ciphertext, p)
print(f"Decrypted message: {decrypted_message}")
