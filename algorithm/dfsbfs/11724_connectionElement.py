import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline


def bfs(v, graph, visit):
    queue=deque([v])
    visit[v]=True

    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if not visit[i]:
                queue.append(i)
                visit[i]=True

def dfs(v, graph, visit):
    visit[v]=True

    for i in graph[v]:
        if not visit[i]:
            dfs(i, graph, visit)



n, m = map(int, input().split())
graph=[[] for i in range(n+1)]
visit=[False for i in range(n+1)]
for _ in range(m):
    idx1, idx2 = map(int, input().split())
    graph[idx1].append(idx2)
    graph[idx2].append(idx1)

# print(graph)

answer=0
for i in range(1, n+1):
    if not visit[i]:
        # bfs(i, graph, visit)
        dfs(i, graph, visit)
        answer+=1
print(answer)