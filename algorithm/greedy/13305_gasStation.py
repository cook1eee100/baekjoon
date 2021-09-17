n = int(input())
oilList = list(map(int, input().split()))
cityList = list(map(int, input().split()))

answer=0
oilPrice=cityList[0]
for i in range(len(oilList)):
    if i==0:
        answer+=oilPrice*oilList[i]
    else:
        if oilPrice < cityList[i]:
            answer+=oilPrice*oilList[i]
        else:
            oilPrice=cityList[i]
            answer+=oilPrice*oilList[i]
print(answer)