import sys
from collections import deque
input = sys.stdin.readline


def dfs(v, graph, visit):
    global cnt
    visit[v]=True
    for i in graph[v]:
        if not visit[i]:
            cnt+=1
            dfs(i, graph, visit)


def bfs(v, graph, visit):
    queue = deque([v])
    visit[v]=True
    count=0
    while queue:
        p = queue.popleft()
        count+=1
        for i in graph[p]:
            if not visit[i]:
                queue.append(i)
                visit[i]=True
    return count


n = int(input())
m = int(input())

graph=[[] for i in range(n+1)]
visit=[False for i in range(n+1)]
for i in range(m):
    num1, num2 = map(int, input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)

for i in range(n+1):
    graph[i].sort()

# print(graph)
# print(visit)
cnt=0
dfs(1, graph, visit)
print(cnt)
# print(bfs(1, graph, visit)-1)