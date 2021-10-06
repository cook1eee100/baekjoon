import sys
input = sys.stdin.readline

n= int(input())
pointList=[]
for i in range(n):
    pointList.append(list(map(int, input().split())))

print(pointList)


