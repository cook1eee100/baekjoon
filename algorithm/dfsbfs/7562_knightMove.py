import sys
from collections import deque
input = sys.stdin.readline


d = [[-2,1], [-1,2], [1,2], [2,1], [2,-1], [1,-2], [-1,-2], [-2,-1]]

def bfs(sx, sy, ex, ey, graph):
    queue = deque()
    queue.append([sx, sy, 0])
    s=set()
    s.add((sx, sy))

    while queue:
        x, y, count = queue.popleft()
        if x==ex and y==ey:
            return count
        
        else:
            count+=1
            for i in range(len(d)):
                nx = x+d[i][0]
                ny = y+d[i][1]

                if (0<=nx<len(graph) and 0<=ny<len(graph)) and (nx, ny) not in s:
                    queue.append([nx, ny, count])
                    s.add((nx, ny))

    return -1
    

t=int(input())
for _ in range(t):
    l=int(input())
    graph=[[0 for i in range(l)] for j in range(l)]
    visit=[[False for i in range(l)] for j in range(l)]
    sx, sy = map(int ,input().split())
    ex, ey = map(int, input().split())

    answer=bfs(sx, sy, ex, ey, graph)
    print(answer)

