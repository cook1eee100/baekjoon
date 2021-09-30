import sys
input = sys.stdin.readline

n=int(input())
consultingList=[]
for _ in range(n):
    consultingList.append(list(map(int,input().split())))

print(consultingList)