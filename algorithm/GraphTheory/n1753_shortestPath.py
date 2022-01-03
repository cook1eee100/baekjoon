import sys
from collections import deque
input = sys.stdin.readline


def bfs(start, end, graph):
    visit=[False for _ in range(len(graph))]
    queue = deque()
    queue.append([start, 0])
    visit[start]=True

    while queue:
        v, c = queue.popleft()
        if v==end:
            return c

        for i in range(len(graph[v])):
            if not visit[graph[v][i][0]]:
                queue.append([graph[v][i][0], c+graph[v][i][1]])
                visit[graph[v][i][0]]=True

    return -1


v, e = map(int, input().split())
start=int(input())
graph=[[] for _ in range(v+1)]
for _ in range(e):
    s, e, w = map(int, input().split())
    graph[s].append([e, w])
#print(graph)

answer=[]
for i in range(1, v+1):
    answer.append(bfs(start, i, graph))

for i in answer:
    if i==-1:
        print("INF")
    else:
        print(i)