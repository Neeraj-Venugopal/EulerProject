# '''
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?
# '''

def is_prime(n):
    if n < 2:
        return False
    i = 2
        while (i * i <= n):
        if n % i == 0:
            return False
        i = i + 1
    return True

def n_prime(n):
    i = 2
    while n > 0:
        if is_prime(i):
            n = n - 1
            if n == 0:
                return i
        i = i + 1
    return -1

if __name__ == '__main__':
    print n_prime(10001)
