import sys
from collections import deque
input = sys.stdin.readline


n1, n2 = map(int, input().split())
n1List = list(input().rstrip())
n2List = list(input().rstrip())
t= int(input())

n1List.reverse()
antList=n1List+n2List
visit=[0 for i in range(len(antList))]

for i in range(len(antList)-len(n2List), len(antList)):
    visit[i]=1

for time in range(t):
    temp=0
    for i in range(1,len(antList)):
        # print(i, antList)
        if visit[i]==1 and visit[i-1]==0:
            if temp<time+1 and temp<len(n1List):
                antList[i], antList[i-1] = antList[i-1], antList[i]
                visit[i], visit[i-1] = visit[i-1], visit[i]
                temp+=1
        # print(i, antList)

for i in antList:
    print(i, end="")