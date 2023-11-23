def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False 

    for number in range(2, int(limit**0.5) + 1):
        if is_prime[number]:
            for multiple in range(number * number, limit + 1, number):
                is_prime[multiple] = False

    primes = [number for number in range(2, limit + 1) if is_prime[number]]
    return primes

limit = 1000
prime_numbers = sieve_of_eratosthenes(limit)
prime_sum = sum(prime_numbers)
print(f"The sum of prime numbers between 0 and 1000 is: {prime_sum}")
