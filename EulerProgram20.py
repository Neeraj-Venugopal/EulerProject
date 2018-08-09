"""
For example, 10! = 3628800
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

product = 1

for i in range(1, 101):
    product *= i

sum = 0

while product > 0:
    sum += product % 10
    product /= 10

print sum

