import sys
from collections import deque
input = sys.stdin.readline




if __name__=="__main__":
    n, k = map(int, input().split())
    graph=[list(map(int, input().split())) for _ in range(n)]
    s, x, y = map(int, input().split())
    queue=deque()


    for idx_k in range(1, k+1):
        for i in range(n):
            for j in range(n):
                if graph[i][j]==idx_k:
                    queue.append([i,j,0])
    
    while queue:
        i, j, t= queue.popleft()

        if t==s:
            break

        dx=[0,1,0,-1]
        dy=[1,0,-1,0]

        for idx in range(4):
            nx = i+dx[idx]
            ny = j+dy[idx]

            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==0:
                graph[nx][ny]=graph[i][j]
                queue.append([nx,ny,t+1])

    print(graph[x-1][y-1])