import sys
from collections import deque
input = sys.stdin.readline


def dfs(a):
    for i in range(len(a)):
        a[i]+=1

    dfs(a)

a=[1,2,3,4]

dfs(a)