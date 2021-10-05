n, m = map(int, input().split())
cardList=list(map(int, input().split()))

answer=0
for idx1 in range(len(cardList)-2):
    for idx2 in range(idx1+1, len(cardList)-1):
        for idx3 in range(idx2+1, len(cardList)):
            temp = cardList[idx1]+cardList[idx2]+cardList[idx3]
            if answer< temp <= m:
                answer=temp

print(answer)


