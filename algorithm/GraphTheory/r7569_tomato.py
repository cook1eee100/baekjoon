import sys
from collections import deque
input = sys.stdin.readline





m, n, h = map(int, input().split())
queue = deque()
graph=[]

for idx_h in range(h):
    graph.append([])
    for idx_n in range(n):
        temp = list(map(int, input().split()))
        graph[idx_h].append(temp)

        for idx_m in range(m):
            if temp[idx_m]==1:
                queue.append([idx_n, idx_m, idx_h])

# print(graph)


while queue:
    
    x, y, z=queue.popleft()

    d=[[0,1,0],[1,0,0],[-1,0,0], [0,-1,0], [0,0,-1], [0,0,1]]

    for i in d:
        nx=x+i[0]
        ny=y+i[1]
        nz=z+i[2]

        if 0<=nx<n and 0<=ny<m and 0<=nz<h:
            if graph[nz][nx][ny]==0:
                graph[nz][nx][ny]=graph[z][x][y]+1
                queue.append([nx, ny, nz])
    

answer=-1
check=0
for idx_h in graph:
    for idx_n in idx_h:
        if 0 in idx_n:
            check=1
            break
        else:
            if answer<max(idx_n):
                answer=max(idx_n)-1

if check:
    print(-1)
else:
    print(answer)



"""
    DfsBfs 폴더 7576 번 비슷한 문제

    graph 에서 확장해 나갈때 같은 값으로 표시하지말고
    이전값에 1을 더해서 1초 지났다는 시간표시를 하기

"""