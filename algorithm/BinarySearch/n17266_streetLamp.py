import sys
input = sys.stdin.readline

n=int(input())
m=int(input())
graph=list(map(int, input().split()))

start=1
end=n

while start<=end:
    mid=(start+end)//2

    check=[0 for _ in range(n+1)]
    