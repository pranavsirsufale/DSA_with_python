def is_prime(num):
    # A prime number is greater than 1
    if num <= 1:
        return False
    
    # Check divisors from 2 to sqrt(num)
    for i in range(2,int(num**0.5) + 1 ):
        if num % i == 0: # if divisible by any number, it's not prime
            return False
    
    return True


number = 5
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")






def find_primes_in_range(start,end):
    primes = []
    for num in range(start,end + 1):
        if is_prime(num):
            primes.append(num)
    for i in primes:
        yield f'{i} is a prime number'

# Example usage
primes = find_primes_in_range(10,50)

for prime in primes:
    print(prime)
    