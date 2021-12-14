import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph=[list(map(int, list(input().strip()))) for _ in range(n) ]

answer=0
for i in range(n):
    for j in range(m):
        squareNum=1
        