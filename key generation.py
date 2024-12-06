def is_prime(n):
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(n**0.5) + 1):  # Check divisibility from 2 to half n
        if n % i == 0:  # If n is divisible by i its not prime
            return False  
    return True  # if no divisors were found n is prime 

def find_primitive_root(p):
    if not is_prime(p):
        return None  

    p1 = p - 1   # Find the prime factors of p-1
    factors = []
    
    for i in range(2, int(p1**0.5) + 1):   # Check for factors from 2 to half p1
        if p1 % i == 0:  # If i is a factor
            factors.append(i)  # Add it to the list of factors
            while p1 % i == 0:  # Remove all occurrences of i
                p1 //= i
    if p1 > 1:  # If p1 is still greater than 1, it's a prime factor
        factors.append(p1)

    # Find a primitive root
    for g in range(2, p):  # Check numbers from 2 to p-1
        is_primitive = True  # Assume g is a primitive root
        for factor in factors:
            if pow(g, (p - 1) // factor, p) == 1: # Check if g^(p-1)/factor ≡ 1 (mod p)
                is_primitive = False  # g is not a primitive root
                break
        if is_primitive:  # If g is a primitive root, return it
            return g

    return None  # Return None if no primitive root is found
