def is_prime(n):
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(n**0.5) + 1):  # Check divisibility from 2 to √n
        if n % i == 0:  # If n is divisible by i its not prime
            return False  
    return True  # if no divisors were found n is prime 
