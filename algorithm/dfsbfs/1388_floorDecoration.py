import sys
input = sys.stdin.readline


def dfs(x, y, graph, visit):
    visit[x][y]=True

    nx=x+1
    ny=y+1
    if graph[x][y]=='-' and ny<len(graph[-1]):
        if graph[x][ny]=='-':
            dfs(x, ny, graph, visit)
    elif graph[x][y]=='|' and nx<len(graph):
        if graph[nx][y]=='|':
            dfs(nx, y, graph, visit)

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input().strip()))
# print(graph)
visit=[[False for i in range(m)] for j in range(n)]
# print(visit)
count=0
for i in range(n):
    for j in range(m):
        if not visit[i][j]:
            dfs(i, j, graph, visit)
            count+=1
print(count)