'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

if __name__ == '__main__':
    limit = 2000000
    numbers = set(xrange(3, limit, 2))

    for num in range(3, int(limit ** 0.5) + 1, 2):
        number = num
        while number < limit:
            number += num
            if number in numbers:
                numbers.remove(number)
    print 2 + sum(numbers)
