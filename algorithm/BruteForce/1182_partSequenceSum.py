import sys
from itertools import combinations
input = sys.stdin.readline

n, s = map(int, input().split())
graph=list(map(int, input().split()))

count=0

for i in range(1, n+1):
    temp = combinations(graph, i)    
    
    for com in temp:
        if sum(com)==s:
            count+=1
print(count)