import sys
input = sys.stdin.readline

n, m = map(int, input().split())

cardList = list(map(int, input().split()))



for i in range(m):
    cardList.sort()
    sum = cardList[0]+cardList[1]
    cardList[0]=cardList[1]=sum

answer=0
for i in cardList:
    answer+=i

print(answer)