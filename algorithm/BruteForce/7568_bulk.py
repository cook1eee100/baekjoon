import sys
input = sys.stdin.readline

n = int(input())
peopleList=[]
for _ in range(n):
    peopleList.append(list(map(int, input().split())))

answer=[1 for i in range(n)]
for idx1 in range(len(peopleList)):
    for idx2 in range(len(peopleList)):
        if peopleList[idx1][0]<peopleList[idx2][0] and peopleList[idx1][1]<peopleList[idx2][1]:
            answer[idx1]+=1

for i in answer:
    print(i, end=" ")