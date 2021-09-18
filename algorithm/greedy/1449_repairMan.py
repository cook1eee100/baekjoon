n, l = map(int, input().split())
waterList = list(map(int, input().split()))

waterList.sort()

answer=standard=0
for i in range(len(waterList)):
    if i==0:
        standard=waterList[i]-0.5
        answer+=1
    else:
        if standard+l < waterList[i]+0.5:
            standard = waterList[i]
            answer+=1
print(answer)

