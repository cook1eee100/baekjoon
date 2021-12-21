import sys
input = sys.stdin.readline

t=int(input())
graph=[]
for _ in range(t):
    graph.append(list(input().strip()))

for i in range(t):
    count=0
    