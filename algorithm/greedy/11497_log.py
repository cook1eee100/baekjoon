import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n=int(input())
    logList=list(map(int, input().split()))
    logList.sort()
    result=0
    for j in range(2, n):
        result=max(result, abs(logList[j]-logList[j-2]))
    print(result)