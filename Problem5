'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

import math as m

def lcm(value1, value2):
    temp1 = value1
    temp2 = value2

    while (value2):  # GCD Calculation
        value1, value2 = value2, value1 % value2

    lcmOut = temp1 * temp2 / value1  # LCM = Number1 * Number2 / GCD
    return lcmOut

def callFunction(number):
    counter = number;
    answer = 1;

    while counter > 1:
        # print "hi"
        # pow(answer, 1, counter)
        if not (pow(answer, 1, counter) == 0):  # pow calculates answer to the power 1 Modulo counter
            answer = lcm(answer, counter)
        # print answer, " \t ", counter
        counter -= 1
    return answer


if __name__ == '__main__':
    print " Enter the Number "
    number = input()
    print callFunction(number)
