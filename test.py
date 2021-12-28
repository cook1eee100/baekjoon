import sys
from collections import deque
input = sys.stdin.readline


def dfs(depth, a, test):
    if depth==3:
        test.append(depth)
        return

    for i in range(len(a)):
        a[i]+=1

    dfs(depth+1, a, test)

a=[1,2,3,4]
test=[]
dfs(0, a, test)
print(a)
print(test)




def test(b):
    b=3

q=2
test(q)
print(q)