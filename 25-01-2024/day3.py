At the annual meeting of Board of Directors of Acme Inc. If everyone attending shakes hands exactly one time with every other attendee, how many handshakes are there?

Example

There are  attendees, ,  and .  shakes hands with  and , and  shakes hands with . Now they have all shaken hands after  handshakes.

Function Description

Complete the handshakes function in the editor below.

handshakes has the following parameter:

int n: the number of attendees
Returns

int: the number of handshakes
Input Format
The first line contains the number of test cases .
Each of the following  lines contains an integer, .

Constraints



Sample Input

2
1
2
Sample Output

0
1
Explanation

Case 1 : The lonely board member shakes no hands, hence 0.
Case 2 : There are 2 board members, so 1 handshake takes place.

Submissions: 131
Max Score: 10
Difficulty: Easy
Rate This Challenge:

    
More
 
    
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
# Complete the 'handshake' function below.
11
#
12
# The function is expected to return an INTEGER.
13
# The function accepts INTEGER n as parameter.
14
#
15
​
16
def handshake(s):
17
    if s<2:
18
       return 0
19
    return math.factorial(s)//(2 * math.factorial(s-2))
20
​
21
if __name__ == '__main__':
22
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
23
​
24
    t = int(input().strip())
25
​
26
    for t_itr in range(t):
27
        n = int(input().strip())
28
​
29
        result = handshake(n)
30
​
31
        fptr.write(str(result) + '\n')
32
​
33
    fptr.close()
34
​
