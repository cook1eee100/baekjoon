import sys
input = sys.stdin.readline

n = int(input())

costList=[]
for _ in range(n):
    costList.append(int(input()))

costList.sort(reverse=True)
answer=0
for i in range(len(costList)):
    if i%3!=2:
        answer+=costList[i]

print(answer)

