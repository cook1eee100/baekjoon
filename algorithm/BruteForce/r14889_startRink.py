import sys
input = sys.stdin.readline
from itertools import combinations

n= int(input())
pointList=[]
for i in range(n):
    pointList.append(list(map(int, input().split())))

# print(pointList)

peopleList = [i for i in range(1, n+1)]
com=list(combinations(peopleList, n//2))
minValue=1e9
for idx in range(len(com)//2):
    startMember=com[idx]
    linkMember=com[-1-idx]
    startTeam=0
    linkTeam=0

    for i in range(len(startMember)):
        for j in range(i, len(startMember)):
            startTeam+=pointList[startMember[i]-1][startMember[j]-1] + pointList[startMember[j]-1][startMember[i]-1]
    
    for i in range(len(linkMember)):
        for j in range(i, len(linkMember)):
            linkTeam+=pointList[linkMember[i]-1][linkMember[j]-1] + pointList[linkMember[j]-1][linkMember[i]-1]
    
    if abs(startTeam-linkTeam)<minValue:
        minValue=abs(startTeam-linkTeam)

print(minValue)

"""
from itertools import combinations 조합
from itertools import permutations 순열

짝수 개수로 조합을 짜면 맨 처음꺼와 맨 뒤에꺼가 대칭, 맨처음꺼+1 와 맨 뒤에거-1이 대칭 ....

"""