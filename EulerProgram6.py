'''
The sum of the squares of the first ten natural numbers is, 12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)2 = 552 = 3025

Find the difference between the sum of the squares of the first one hundred natural
numbers and the square of the sum.
'''

# To find Summation of n and then square it, n * (n + 1) / 2
# To find Summation of n square, n * (n + 1) * ( 2n + 1 ) / 6

class problemClass:
    def __init__(self, number):
        self.sumOfN = number
        self.sumOfNsq = number
        self.sumOfNsqaure = number

    def summationOfFirstNNumbers(self):
        num = self.sumOfN
        self.sumOfN = num * (num + 1)/2
        # print self.sumOfN
        return

    def sqaureOfFirstNnumbers(self):
        num = self.sumOfN
        self.sumOfNsq = num * num
        # print self.sumOfNsq
        return

    def summationOfFirstNSqaureNumbers(self):
        num = self.sumOfNsqaure
        self.sumOfNsqaure = num * (num + 1) * ((2 * num) + 1) / 6
        # print self.sumOfNsqaure
        return

    def printClass(self):
        return  self.sumOfNsq - self.sumOfNsqaure

if __name__ == '__main__':

    print "Enter the Limit to N natural Numbers"
    number = input()

    myObject = problemClass(number)
    myObject.summationOfFirstNNumbers()
    myObject.sqaureOfFirstNnumbers()
    myObject.summationOfFirstNSqaureNumbers()

    print myObject.printClass()
