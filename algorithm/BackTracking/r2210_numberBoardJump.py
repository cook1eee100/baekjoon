"""   내가 푼거 성공함 bfs방식
import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y, graph, answer):
    queue = deque()
    queue.append([x, y, [graph[x][y]]])

    dx=[1, 0, -1, 0]
    dy=[0, 1, 0, -1]

    while queue:
        temp = queue.popleft()
        x, y, l = temp[0], temp[1], temp[2]
        if len(l)==6:
            if l not in answer:
                answer.append(l)
        else:
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]

                if 0<=nx<5 and 0<=ny<5:
                    l.append(graph[nx][ny])
                    templ=l[:]
                    queue.append([nx, ny, templ])
                    l.pop()
        

graph=[list(map(int, input().split())) for _ in range(5)]

answer=[]
for i in range(5):
    for j in range(5):
        bfs(i, j, graph, answer)
print(len(answer))
"""


# dfs방식
import sys
input =sys.stdin.readline


def dfs(x, y, graph, out, answer):
    if len(out)==6:
        if out not in answer:
            answer.append(out)
        return

    dx=[0, 1, 0, -1]
    dy=[1, 0, -1, 0]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<5 and 0<=ny<5:
            dfs(nx, ny, graph, out+[graph[nx][ny]], answer)
            

graph = [list(map(int, input().split())) for _ in range(5)]


answer=[]
for i in range(5):
    for j in range(5):
        dfs(i, j, graph, [graph[i][j]], answer)

print(len(answer))

"""
# dfs 방식에서
    out 에 append 했다가 처리 한 후 pop 을 하면 값들이 다 사라짐
    그래서 애초에 재귀할 때 인자값으로 리스트를 더해서 함수 호출함으로 써 값 사라지는거 방지
"""