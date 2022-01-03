import sys
from collections import deque
input = sys.stdin.readline


def bfs(s, graph):
    visit=[False for _ in range(len(graph))]
    queue = deque()
    queue.append(s)
    visit[s]=True

    c=1
    while queue:
        s= queue.popleft()

        for i in graph[s]:
            if not visit[i]:
                queue.append(i)
                visit[i]=True
                c+=1
    return c

n, m = map(int, input().split())

graph=[[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
# print(graph)

answer=[]
for i in range(1, n+1):
    answer.append(bfs(i, graph))

for i in range(len(answer)):
    if answer[i]==max(answer):
        print(i+1, end=" ")


"""

    # 18~20 line 부분
    
    최단 거리 개수는 queue 에 c 넣어서 c+1 로 증가시키고
    퍼지는거는 해당하는 노드들이 나올때마다 +1

"""