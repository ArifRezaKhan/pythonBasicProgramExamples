# To print all primes smaller than or equal to n using
# Sieve of Eratosthenes (Time Complexity: o(n*log(log(n))))


def sieve_of_eratosthenes(num):
    # Create a boolean array "prime[0...n]" and initialize
    # all entries it as true. A value in prime[i] will finally be
    # false if i is NOT a prime, else true.

    prime = [True for i in range(n+1)]
    p = 2
    while p * p <= n:
        # If prime[p] is not changed, then it is a prime
        if prime[p]:
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    # Print all prime numbers
    for p in range(2, n):
        if prime[p]:
            print(p)


# Driver program
if __name__ == '__main__':
    n = 10
    print("Following are the primes smaller than or equal to", n, ":")
    sieve_of_eratosthenes(n)
