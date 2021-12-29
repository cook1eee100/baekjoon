import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = [input().strip() for _ in range(n)]

graph = [input().strip() for _ in range(m)]

count=0
for i in graph:
    if i in s:
        count+=1

print(count)