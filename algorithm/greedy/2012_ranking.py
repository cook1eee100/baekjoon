import sys
input = sys.stdin.readline

n = int(input())

rankingList=[]
for i in range(n):
    rankingList.append(int(input()))

answer=0
rankingList.sort()
ranking=1
for i in rankingList:
    answer+=abs(ranking-i)
    ranking+=1
print(answer)