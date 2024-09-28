import tqdm 
import numpy as np

def generate_primes(limit):
    # sieve of eratosthenes
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False

    for num in tqdm.tqdm(range(2, limit + 1)):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    return primes

def rwh_primes1(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * int(n/2)
    for i in tqdm.tqdm(range(3,int(n**0.5)+1,2)):
        if sieve[int(i/2)]:
            sieve[int(i*i/2)::i] = [False] * int((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n/2) if sieve[int(i)]]


def identify_truncatable_prime(prime, primes):
    x = str(prime)
    x_rev = x[::-1]
    for i in range(len(x)):
        for d in [x, x_rev]:
            if int(d[i:]) not in primes: 
                return False
            
        return True

if __name__ == "__main__":
    trunctable_primes = [] 
    # primes = generate_primes(1_000_000_000)
    primes = rwh_primes1(1_000_000_000)
    for prime in tqdm.tqdm(primes):
        if identify_truncatable_prime(prime, primes):
            trunctable_primes.append(prime)
    print(trunctable_primes)



