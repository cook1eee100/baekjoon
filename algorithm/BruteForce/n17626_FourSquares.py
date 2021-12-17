import math
import sys
input =sys.stdin.readline

n=int(input())

temp = int(math.sqrt(n))

count=0
for i in range(temp, 0, -1):
    if n>=i **2:
        count+=1
        n=n-temp**2
print(count)