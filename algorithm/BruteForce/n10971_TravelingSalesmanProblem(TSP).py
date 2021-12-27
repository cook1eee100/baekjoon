import sys
from itertools import permutations
input = sys.stdin.readline

n=int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

per = permutations([0,1,2,3])
minValue=1e9
for p in per:
    total=0
    for i in range(n):
        s,e=p[i], p[(i+1)%n]
        total+=graph[s][e]
    
    if minValue >total:
        minValue=total
print(minValue)