n = int(input())

answer=0
scoreList=[]
for _ in range(n):
    scoreList.append(int(input()))

for i in range(len(scoreList)-1,0,-1):
    if scoreList[i]<=scoreList[i-1]:
        answer+=scoreList[i-1]-(scoreList[i]-1)
        scoreList[i-1]=scoreList[i]-1

print(answer)