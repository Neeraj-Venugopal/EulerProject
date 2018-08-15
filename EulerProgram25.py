"""
The Fibonacci sequence is defined by the recurrence relation:
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

import time

# Fibonacci Series Calculation
def fibonacci(prev, current):
    return current, prev + current


if __name__ == '__main__':
    start = time.time()
    prev = 1
    current = 1
    count = 2
    while True:

        prev, current = fibonacci(prev, current)
        count += 1

        if len(str(current)) >= 1000:
            print count
            break

    print "Time Taken to execute: ", (time.time() - start) * 1000, "ms"


