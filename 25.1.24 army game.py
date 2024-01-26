Luke is daydreaming in Math class. He has a sheet of graph paper with  rows and  columns, and he imagines that there is an army base in each cell for a total of  bases. He wants to drop supplies at strategic points on the sheet, marking each drop point with a red dot. If a base contains at least one package inside or on top of its border fence, then it's considered to be supplied. For example:

image

Given  and , what's the minimum number of packages that Luke must drop to supply all of his bases?

Example


Packages can be dropped at the corner between cells (0, 0), (0, 1), (1, 0) and (1, 1) to supply  bases. Another package can be dropped at a border between (0, 2) and (1, 2). This supplies all bases using  packages.

Function Description

Complete the gameWithCells function in the editor below.

gameWithCells has the following parameters:

int n: the number of rows in the game
int m: the number of columns in the game
Returns

int: the minimum number of packages required
Input Format

Two space-separated integers describing the respective values of  and .

Constraints


Sample Input 0

2 2
Sample Output 0

1
Explanation 0

Luke has four bases in a  grid. If he drops a single package where the walls of all four bases intersect, then those four cells can access the package:

image

Because he managed to supply all four bases with a single supply drop, we print  as our answer.

Submissions: 120
Max Score: 10
Difficulty: Easy
Rate This Challenge:

    
More
 
# r indicates no of columns
1
#!/bin/python3
2
​
3
import math
4
import os
5
import random
6
import re
7
import sys
8
​
9
#
10
# Complete the 'gameWithCells' function below.
11
#
12
# The function is expected to return an INTEGER.
13
# The function accepts following parameters:
14
#  1. INTEGER n
15
#  2. INTEGER m
16
#
17
​
18
def gameWithCells(s,q):
19
    # s indicates no of rows
20
    # r indicates no of columns
21
    packages = math.ceil(s/2)*math.ceil(q/2)
22
    return packages
23
    
24
​
25
if __name__ == '__main__':
26
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
27
​
28
    first_multiple_input = input().rstrip().split()
29
​
30
    n = int(first_multiple_input[0])
31
​
32
    m = int(first_multiple_input[1])
33
​
34
    result = gameWithCells(n, m)
35
​
36
    fptr.write(str(result) + '\n')
37
​
38
    fptr.close()
39
​
