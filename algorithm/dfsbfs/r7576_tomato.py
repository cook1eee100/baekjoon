"""  시간초과
import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y, graph):
    queue = deque()
    queue.append([x,y])

    dx=[0, 1, 0, -1]
    dy=[1, 0, -1, 0]

    while queue:
        x, y = queue.popleft()

        for i in range(len(dx)):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<len(graph) and 0<=ny<len(graph[0]):
                if graph[nx][ny]==0 or graph[nx][ny]> graph[x][y]+1:
                    queue.append([nx, ny])
                    graph[nx][ny]=graph[x][y]+1
    return

m, n = map(int, input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int, input().split())))
# visit=[[0 for _ in range(m)] for _ in range(n)]


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(i, j, graph)
print(graph)

answer= -1
for li in graph:
    if 0 in li:
        print(-1)
        break
    if answer<max(li):
        answer=max(li)

else:
    print(answer-1)
"""


import sys
from collections import deque
input = sys.stdin.readline

queue=deque()
m, n = map(int, input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int, input().split())))

    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i,j])

dx=[1,0,-1,0]
dy=[0,1,0,-1]
while queue:
    x, y=queue.popleft()
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
            queue.append([nx, ny])
            graph[nx][ny] = graph[x][y]+1

# print(graph)
answer=-1
for li in graph:
    if 0 in li:
        print(-1)
        break

    if answer< max(li):
        answer=max(li)
else:
    print(answer-1)



"""
전체 다 탐색해서 시작하는거 보다
입력받을 때 값 체크를 해서 그 값들을 큐에 넣어놓고 그 큐를 반복해서 풀기

"""