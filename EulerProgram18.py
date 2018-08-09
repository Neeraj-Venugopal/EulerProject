# By starting at the top of the triangle below and moving to adjacent numbers on the row below,
# the maximum total from top to bottom is 23.
#    3
#   7 4
#  2 4 6
# 8 5 9 3
# That is, 3 + 7 + 4 + 9 = 23.
# Find the maximum total from top to bottom of the triangle below:
#               75
#              95 64
#             17 47 82
#            18 35 87 10
#           20 04 82 47 65
#          19 01 23 75 03 34
#         88 02 77 73 07 63 67
#        99 65 04 28 06 16 70 92
#       41 41 26 56 83 40 80 70 33
#      41 48 72 33 47 32 37 16 94 29
#     53 71 44 65 25 43 91 52 97 51 14
#    70 11 33 28 77 73 17 78 39 68 17 57
#   91 71 52 38 17 14 91 43 58 50 27 29 48
#  63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
# However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
# it cannot be solved by brute force, and requires a clever method! ;o)

numPyramid = """75\n\
95 64\n\
17 47 82\n\
18 35 87 10\n\
20 04 82 47 65\n\
19 01 23 75 03 34\n\
88 02 77 73 07 63 67\n\
99 65 04 28 06 16 70 92\n\
41 41 26 56 83 40 80 70 33\n\
41 48 72 33 47 32 37 16 94 29\n\
53 71 44 65 25 43 91 52 97 51 14\n\
70 11 33 28 77 73 17 78 39 68 17 57\n\
91 71 52 38 17 14 91 43 58 50 27 29 48\n\
63 66 04 68 89 53 67 30 73 16 69 87 40 31\n\
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

#Testing
# numPyramid="""3\n\
# 7 4\n\
# 2 4 6\n\
# 8 5 9 3"""


import time

if __name__ == '__main__':
    print "Inside Main"
    start = time.time()

    # 2D Matrix in python
    list = [[int(num) for num in line.split()] for line in numPyramid.split("\n")]
    maxList = []

    i = len(list) - 1
    while i >= 0:
        for counter in range(0, len(list[i]) - 1):
            number = max(list[i][counter], list[i][counter + 1])
            maxList.append(number)

        # Adding 2 arrays with equal sizes. Used zip function in python
        list[i-1] = [x + y for x, y in zip(maxList, list[i-1])]

        i -= 1
        maxList = []

    print list[0]
    print "Program End in: ", time.time() - start
