"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order,
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file
"""

import time

start = time.time()

# Read inout from File Section
fileOpen = open('EulerProgram22.txt', 'r')
nameList = []
for word in fileOpen.read().split(","):
    names = word.split("\"")
    nameList.append(names[1])

# Sort the names in the List
nameList = sorted(nameList)

# Create a dictonary from a-z with values 1-26
char = 'a'
alphaDictonary = {}
for i in range(1, 27):
    alphaDictonary[char] = i
    char = chr(ord(char)+1)

# Logic to add characters in the name and multiply with index
index = 1
count = 0
sum = 0

for name in nameList:
    for characters in name:
        characters = characters.lower()
        count += alphaDictonary[characters]

    product = index * count
    sum += product
    index += 1
    count = 0

print sum
print "Total Time: " , 1000 * (time.time() - start), "ms"
