
# 인접 리스트
import sys
from collections import deque
input = sys.stdin.readline


def dfs(v, graph, check):
    print(v, end=" ")
    check[v]=True
    
    for i in graph[v]:
        if not check[i]:
            dfs(i, graph, check)


def bfs(v, graph, check):
    queue=deque()
    queue.append(v)
    check[v]=False
    while queue:
        num = queue.popleft()
        print(num, end=" ")

        for i in graph[num]:
            if check[i]:
                queue.append(i)
                check[i]=False


n, m, v = map(int, input().split())
graph=[[] for i in range(n+1)]
check=[False for i in range(n+1)]
for _ in range(m):
    idx1, idx2 = map(int, input().split())
    graph[idx1].append(idx2)
    graph[idx2].append(idx1)

for i in range(n+1):
    graph[i].sort()


# print(graph)
# print(check)


dfs(v, graph, check)
print()
bfs(v, graph, check)




#---------------------------------------------------
# 인접 행렬

# import sys
# input = sys.stdin.readline

# n, m, v = map(int, input().split())
# graph=[[0 for j in range(n+1)] for i in range(n+1)]
# visit=[False for i in range(n+1)]

# for _ in range(m):
#     x,y = map(int, input().split())
#     graph[x][y]=1
#     graph[y][x]=1

# for idx in graph:
#     print(idx)

