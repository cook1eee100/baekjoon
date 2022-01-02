import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, graph, visit):
    queue = deque()
    queue.append(x)
    
    while queue:
        c = queue.popleft()

        for i in range(len(graph)):
            if graph[c][i]==1 and visit[x][i]==0:
                queue.append(i)
                visit[x][i]=1



def dfs(x, nx, graph, visit):
    for i in range(len(graph)):
        if graph[nx][i]==1 and visit[x][i]==0:
            visit[x][i]=1
            dfs(x, i, graph, visit)
    
    return


n=int(input())
graph=[list(map(int, input().split())) for _ in range(n)]

visit=[[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    # bfs(i, graph, visit)
    dfs(i, i, graph, visit)

print()
for i in range(n):
    for j in range(n):
        print(visit[i][j], end=" ")
    print()



"""
    플로이드-워셜 알고리즘      참고 사이트 https://jay-ji.tistory.com/24


"""