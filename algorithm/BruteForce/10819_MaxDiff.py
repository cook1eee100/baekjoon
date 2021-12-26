import sys
from itertools import permutations
input = sys.stdin.readline

n=int(input())
graph=list(map(int, input().split()))


per = permutations(graph)
max=0
for p in per:
    total=0
    for idx in range(n-1):
        total+=abs(p[idx]-p[idx+1])

    if max<total:
        max=total
print(max)