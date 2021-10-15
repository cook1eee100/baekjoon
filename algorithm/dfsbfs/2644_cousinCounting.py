import sys
from collections import deque
input = sys.stdin.readline


def bfs(a, b, graph, visit):
    queue=deque()
    queue.append([a, 0])
    visit[a]=True
    
    while queue:
        v, count = queue.popleft()
        if v==b:
            return count

        count+=1
        for i in graph[v]:
            if not visit[i]:
                queue.append([i, count])
                visit[i]=True

    return -1

def dfs(a, b, graph, check):
    for i in graph[a]:
        if check[i] ==0:
            check[i]=check[a]+1
            dfs(i, b, graph, check)

n=int(input())
a, b = map(int, input().split())
m=int(input())
graph=[[] for i in range(n+1)]
visit=[False for i in range(n+1)]
check=[0 for i in range(n+1)]
for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n+1):
    graph[i].sort()

# print(graph)

# print(bfs(a, b, graph, visit))

dfs(a, b, graph, check)
print(check[b] if check[b] > 0 else -1)