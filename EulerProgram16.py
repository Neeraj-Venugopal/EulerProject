'''
2 power 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2 power 1000?
'''


import math

# 3
# k = 6 + 5 + 5 + 3 + 6

num = pow(2, 1000)
list = []

while num > 0:
    list.append(num % 10)
    num /= 10

print sum(list)

