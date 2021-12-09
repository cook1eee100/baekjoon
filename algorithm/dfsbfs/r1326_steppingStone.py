import sys
from collections import deque
input = sys.stdin.readline


"""
def bfs(x, y, graph, visitList):
    answer=-1

    queue = deque()
    queue.append([x, 1])
    visitList[x]=1

    d=[1,-1]
    while queue:
        x, count = queue.popleft()
        if (y-x)%graph[x]==0:
            return count
        
        for i in range(len(d)):
            nx = x+d[i]*graph[x]
            if 0<=nx<len(graph) and visitList[nx]==0:
                queue.append([nx, count+1])
                visitList[nx]=1

    return answer
"""


def bfs(x, y, graph, n):
    answer=-1

    visitList=[-1 for i in range(n)]

    queue = deque()
    queue.append(x)
    visitList[x]=0

    while queue:
        node = queue.popleft()
        for i in range(n):
            if (i-node)%graph[node]==0 and visitList[i]==-1:
                queue.append(i)
                visitList[i]= visitList[node]+1
                if i==y:
                    return visitList[i]

    return -1


n = int(input())
graph=list(map(int, input().split()))
a, b=map(int, input().split())

# visitList=[0 for i in range(n)]
# answer = bfs(a-1, b-1, graph, visitList)

answer = bfs(a-1, b-1, graph, n)
print(answer)


"""
방문 리스트를 만들어서 해당 노드들의 카운트를 1씩 증가시키면서 카운트 세기
        
        for i in range(n):
            if (i-node)%graph[node]==0 and visitList[i]==-1:  
이 부분은 현재 노드에서 방문하지 않은 돌덩이 중에 갈 수 있는 노드들을 확인해서 현재 돌덩이에 올수 있는 수에 1을 더하는 부분
"""