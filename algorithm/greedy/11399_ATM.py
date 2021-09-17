n = int(input())
pList = list(map(int, input().split()))

pList.sort()

answer=0
for i in range(len(pList)):
    total=0
    for j in range(0, i+1):
        total+=pList[j]
    answer+=total

print(answer)