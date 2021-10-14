import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline

dx=[0, 1, 0, -1]
dy=[-1, 0, 1, 0]

def bfs(i, j, graph):
    queue = deque()
    queue.append([i, j])
    graph[i][j]=0
    

    while queue:
        y, x = queue.popleft()
        
        for idx in range(4):
            nx=x+dx[idx]
            ny=y+dy[idx]

            if 0>nx or nx>=len(graph[-1]) or 0>ny or ny>=len(graph):
                continue

            if graph[ny][nx]==1:
                queue.append([ny, nx])
                graph[ny][nx]=0

def dfs(i, j, graph):
    graph[i][j]=0
    
    for idx in range(4):
        ni=i+dy[idx]
        nj=j+dx[idx]
        
        if 0<=ni<len(graph) and 0<=nj<len(graph[-1]) and graph[ni][nj]==1:
            dfs(ni, nj, graph)

    # if i<0 or i>=len(graph) or j<0 or j>=len(graph[-1]):
    #     return

    # if graph[i][j]==0:
    #     return

    # graph[i][j]=0

    # dfs(i-1, j, graph)
    # dfs(i, j+1, graph)
    # dfs(i+1, j, graph)
    # dfs(i, j-1, graph)

t=int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph=[[0 for i in range(m)] for i in range(n)]
    # print(graph)

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    # for idx in graph:
    #     print(idx)

    answer=0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                # bfs(i, j, graph)
                dfs(i, j, graph)
                answer+=1
    print(answer)