import sys
from collections import deque
input =sys.stdin.readline


def bfs(v, graph, visit):
    queue = deque([v])
    visit[v]=True
    answerList=[]

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visit[i]:
                queue.append(i)
                answerList.append([i, v])
                visit[i]=True
    
    return answerList
    
n = int(input())
graph =[[] for i in range(n+1)]
visit=[False for i in range(n+1)]
for _ in range(n-1):
    idx1, idx2 = map(int, input().split())
    graph[idx1].append(idx2)
    graph[idx2].append(idx1)

for i in range(1, n+1):
    graph[i].sort()
# print(graph)

answer=bfs(1, graph, visit)
answer.sort()
for a, b in answer:
    print(b)


"""
answer 리스트 새로 할 필요없이
visit 리스트를 0으로 생성해놓고 방문할때 부모노드의 값을 바로넣으면 됨
어차피 visit[i] 값이 0이면 방문x   0이 아니면 방문했음

"""