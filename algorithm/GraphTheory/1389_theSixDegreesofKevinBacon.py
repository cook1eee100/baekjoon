import sys
from collections import deque
input = sys.stdin.readline


def bfs(s, end, graph):
    visit=[False for _ in range(n+1)]
    queue = deque()
    queue.append([s, 0])
    visit[s]=True


    while queue:
        if s==end:
            break
        s, c=queue.popleft()
        for i in graph[s]:
            if not visit[i]:
                queue.append([i, c+1])
                visit[i]=True
    return c


n, m = map(int, input().split())
graph =[[] for _ in range(n+1)]

for _ in range(m):
    num1, num2 = map(int, input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)
# print(graph)

answer=[]
for i in range(1, n+1):
    total=0
    for j in range(1, n+1):
        if i!=j:
            # print(i, j, bfs(i, j, graph))
            total+=bfs(i,j, graph)
    answer.append(total)

for i in range(n):
    if answer[i]==min(answer):
        print(i+1)
        break









"""

# dfs 문제 실패

def dfs(s, end, graph, out, answer):
    if s==end:
        answer.append(len(out))
        return

    for i in graph[s]:
        if i not in out:
            out.append(i)
            dfs(i, end, graph, out, answer)
            out.pop()



n, m = map(int, input().split())
graph =[[] for _ in range(n+1)]

for _ in range(m):
    num1, num2 = map(int, input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)


# print(graph)
answerList=[]
for i in range(1, n+1):
    total=0
    
    for j in range(1, n+1):
        answer=[]
        if i!=j:
            dfs(i, j, graph, [i], answer)

            total+=min(answer)
    answerList.append(total)

for i in range(n):
    if answerList[i]==min(answerList):
        print(i+1)
        break
"""