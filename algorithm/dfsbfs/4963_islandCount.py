import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(99999)

def bfs(x, y, islandList, visitList):
    queue = deque()
    queue.append([x, y])
    visitList[x][y]=1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0<= x-i < len(islandList) and 0<=y-j<len(islandList[0]):
                    if visitList[x-i][y-j]==0 and islandList[x-i][y-j]==1:
                        queue.append([x-i, y-j])
                        visitList[x-i][y-j]=1


# 런타임 에러
def dfs(x, y, islandList, visitList):
    visitList[x][y]=1

    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0<= x-i < len(islandList) and 0<=y-j<len(islandList[0]):
                if visitList[x-i][y-j]==0 and islandList[x-i][y-j]==1:
                    dfs(x-i, y-j, islandList, visitList)
    return

while True:
    w, h = map(int, input().split())
    if w==0 and h==0:
        break

    islandList=[]
    visitList=[[0 for i in range(w)] for j in range(h)]
    for i in range(h):
        islandList.append(list(map(int, input().split())))

    # print(islandList)
    # print(visitList)

    count=0
    for i in range(h):
        for j in range(w):
            if visitList[i][j]==0 and islandList[i][j]==1:
                # bfs(i,j,islandList, visitList)
                dfs(i,j,islandList, visitList)
                count+=1
    print(count)



"""
dfs 런타임 에러
sys.setrecursionlimit(99999) 추가함으로 써 재귀 횟수 제한 걸어서 안나는듯?
"""