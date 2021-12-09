import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(99999)



def bfs(x, y, mazeList):
    queue = deque()
    queue.append([x, y])

    dx=[1, 0, -1, 0]
    dy=[0, 1, 0, -1]
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<len(mazeList) and 0<=ny<len(mazeList[0]) and mazeList[nx][ny] == 1:
                queue.append([nx, ny])
                mazeList[nx][ny]=mazeList[x][y]+1
    
# 시간 초과
def dfs(x, y, mazeList, visitList):
    
    dx=[0, -1, 0, 1]
    dy=[1, 0, -1, 0]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<len(mazeList) and 0<=ny<len(mazeList[0]) and mazeList[nx][ny]==1:
            if visitList[nx][ny] ==0 or visitList[nx][ny] > visitList[x][y]+1:
                visitList[nx][ny]=visitList[x][y]+1
                if nx == len(mazeList) and ny == len(mazeList[0]):
                    return
                dfs(nx, ny, mazeList, visitList)
    return
    
n, m = map(int, input().split())
mazeList=[]
for i in range(n):
    mazeList.append(list(map(int, list(input().strip()))))

visitList=[[0 for i in range(m)] for i in range(n)]
visitList[0][0]=1

# bfs 풀이
# bfs(0, 0, mazeList)
# print(mazeList[n-1][m-1])


dfs(0, 0, mazeList, visitList)
print(visitList[n-1][m-1])




"""
dfs 런타임 에러
sys.setrecursionlimit(99999) 추가함으로 써 재귀 횟수 제한 걸어서 안나는듯?
"""