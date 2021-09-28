import sys
input = sys.stdin.readline

n=int(input())
numList=list(map(int,input().split()))

dpList=[0 for i in range(n+1)]
start=0
for i in range(1, n+1):
    dpList[i] = max(numList[i-1], numList[i-1]+dpList[i-1])

print(max(dpList[1:]))


"""
이전합과 자기값과 체크해서 자기값이 더 크면 그때부터 다시 시작하는 방식
"""