import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y, graph, visit):
    queue = deque()
    queue.append([x, y])
    visit[x][y]=1

    dx=[1,0,-1,0]
    dy=[0,1,0,-1]

    count=1
    while queue:
        x, y = queue.popleft()
        
        for i in range(len(dx)):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<len(graph) and 0<=ny<len(graph[0]):
                if graph[nx][ny]==0 and visit[nx][ny]==0:
                    queue.append([nx, ny])
                    visit[nx][ny]=1
                    count+=1

    return count



n, m, k = map(int, input().split())

graph=[[0 for _ in range(m)] for _ in range(n)]
for _ in range(k):
    m1, n1, m2, n2 = map(int, input().split())

    for idx_n in range(n1, n2):
        for idx_m in range(m1, m2):
            graph[idx_n][idx_m]+=1

graph.reverse()
visit=[[0 for _ in range(m)] for _ in range(n)]

answer=[]
count=0
for i in range(n):
    for j in range(m):
        if graph[i][j]==0 and visit[i][j]==0:
            answer.append(bfs(i, j, graph, visit))
            count+=1

answer.sort()
print(count)
for i in answer:
    print(i, end=" ")