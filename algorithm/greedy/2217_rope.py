n = int(input())
answer=0

ropeList=[]
for _ in range(n):
    ropeList.append(int(input()))

ropeList.sort(reverse=True)

for i, value in enumerate(ropeList):
    total = value*(i+1)
    if i==0:
        answer = total

    else:
        if answer < total:
            answer = total

print(answer)