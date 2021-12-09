import sys
from collections import deque
input = sys.stdin.readline




def bfs(x, y, graph, visit, n):
    queue = deque()
    queue.append([x, y])
    visit[x][y]=1

    dx=[0, -1, 0, 1]
    dy=[1, 0, -1, 0]

    count=1
    while queue:
        x, y = queue.popleft()

        for i in range(len(dx)):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==1 and visit[nx][ny]==0:
                queue.append([nx, ny])
                visit[nx][ny]=1
                count+=1
    
    return count



n = int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int, list(input().strip()))))

visit=[[0 for _ in range(n)] for _ in range(n)]

count=0
answer=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==1 and visit[i][j]==0:
            count+=1
            answer.append(bfs(i, j, graph, visit, n))

print(count)
answer.sort()
for i in answer:
    print(i)

