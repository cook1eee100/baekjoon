import sys
from collections import deque
input =sys.stdin.readline


# def bfs(s, graph):
#     visit=[False for _ in range(len(graph)+1)]
#     queue=deque()
#     queue.append([s,0])
#     visit[s]=True

#     answer=[s]
#     while queue:
#         v,c = queue.popleft()

#         if c==2:
#             break

#         for i in graph[v]:
#             if not visit[i]:
#                 queue.append([i, c+1])
#                 visit[i]=True
#                 answer.append(i)

#     return answer

def bfs(s, graph):
    visit=[0]*(n+1)
    queue = deque([s])
    visit[s]=1


    while queue:
        v=queue.popleft()
        
        for i in graph[v]:
            if not visit[i]:
                visit[i] = visit[v]+1
                queue.append(i)
    return visit


n=int(input())
m=int(input())
graph=[[]for i in range(n+1)]
visit=[ False for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

# answer=bfs(1, graph)
# print(len(answer)-1)

print(bfs(1, graph))
