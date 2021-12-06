import sys
input = sys.stdin.readline

n=int(input())
rgbList=[]
for i in range(n):
    rgbList.append(list(map(int, input().split())))

dpList=[0]
for i in range(1, n):
    rgbList[i][0]=min(rgbList[i-1][1], rgbList[i-1][2])+rgbList[i][0]
    rgbList[i][1]=min(rgbList[i-1][0], rgbList[i-1][2])+rgbList[i][1]
    rgbList[i][2]=min(rgbList[i-1][0], rgbList[i-1][1])+rgbList[i][2]

print(min(rgbList[n-1][0], rgbList[n-1][1], rgbList[n-1][2]))



"""
처음부터 모든 경우의 최솟값을 찾아감

"""