import sys
input = sys.stdin.readline

n = int(input())
sequenceList = list(map(int, input().split()))

dpList=[1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if sequenceList[j]>sequenceList[i]:
            dpList[i] = max(dpList[i], dpList[j]+1)
    
print(max(dpList))