import random
p = int(input("Enter your prime number: "))
g = int(input("Enter your primitive root: "))
h = int(input("Enter your public key: "))
public_key = (p, g, h)
message = input("Enter your message: ")

def encrypt_message(public_key, message):
    ciphertext = []
    for char in message:
        k = random.randint(1, p - 2)  # Choose a random ephemeral key k
        message_int = ord(char)  # Convert the character to an integer

        c1 = pow(g, k, p)  # c1 = (g^k) mod p
        c2 = (message_int * pow(h, k, p)) % p  # c2 = (m * (h^k)) mod p
        ciphertext.append((c1, c2)) # Define the ciphertext

    return ciphertext

ciphertext = encrypt_message(public_key, message)
print(f"Ciphertext: {ciphertext}")
