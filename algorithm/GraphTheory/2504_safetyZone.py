import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y, h, graph, visit):
    queue = deque()
    queue.append([x,y])
    visit[x][y]=1

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    
    while queue:
        x, y = queue.popleft()

        for i in range(len(dx)):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<len(graph) and 0<=ny<len(graph):
                if graph[nx][ny] >h and visit[nx][ny]==0:
                    queue.append([nx, ny])
                    visit[nx][ny]=1






n = int(input())
graph = [ list(map(int, input().split())) for _ in range(n)]


maxValue=0
for i in range(n):
    if maxValue<max(graph[i]):
        maxValue=max(graph[i])

answer=[]
for h in range(0, maxValue):
    visit = [[ 0 for _ in range(n)] for _ in range(n)]
    count=0
    for i in range(n):
        for j in range(n):
            if graph[i][j]>h and visit[i][j]==0:
                bfs(i, j, h, graph, visit)
                count+=1

    answer.append(count)
print(max(answer))