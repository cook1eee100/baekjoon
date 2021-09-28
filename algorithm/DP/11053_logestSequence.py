import sys
input = sys.stdin.readline

n=int(input())
numList=list(map(int, input().split()))

dpList=[1]*(n+1)
for i in range(2, n+1):
    for j in range(1, i):
        if numList[i-1]>numList[j-1]:
            dpList[i] = max(dpList[i], dpList[j]+1)
print(max(dpList))




"""
지금까지의 수와 지금 수를 비교해서 크면 해당수에서의 값을 1 증가시킴?
"""