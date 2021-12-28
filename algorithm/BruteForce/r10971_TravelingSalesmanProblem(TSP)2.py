""" 시간 초과
import sys
input = sys.stdin.readline


def dfs(depth, n, i, out, graph, total):
    global minValue
    if depth==n-1:
        minValue=min(minValue, total+graph[i][out[0]])

        return
    
    for j in range(n):

        if graph[i][j] !=0 and j not in out:
            out.append(j)
            dfs(depth+1, n, j, out, graph, total+graph[i][j])
            out.pop()

n=int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
out=[]

minValue=1e9
total=0
depth=0
for i in range(n):
    out.append(i)
    dfs(depth, n, i, out, graph, total)
    out.pop()

print(minValue)
"""

import sys
input = sys.stdin.readline


def dfs(start, next, total, out, n, graph):
    global minValue

    if len(out)==n:
        if graph[next][start] !=0:
            minValue=min(minValue, total+graph[next][start])
        return

    for i in range(n):
        if graph[next][i]!=0 and i not in out and total<minValue:
            out.append(i)
            dfs(start, i, total+graph[next][i], out, n, graph)
            out.pop()



n=int(input())
graph=[list(map(int, input().split())) for _ in range(n)]

minValue=1e9

for i in range(n):
    dfs(i, i, 0, [i], n, graph)

print(minValue)


"""
    1. 탐색 과정에서 풀이 하기           탐색 끝나고 나서 후보들을 모아서 다시 계산하지 말고

    2. 총합 계산을 각 과정에서 더해가며 끝에 도달했을때 총합 값으로 풀이

    3. 최소값보다 클 경우 실행안되게 
"""