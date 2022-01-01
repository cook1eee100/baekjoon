import sys
input = sys.stdin.readline


def dfs(city, visit, graph, count):

    visit[city]=True

    for i in graph[city]:
        if visit[i]==False:
            count = dfs(i, visit, graph, count+1)

    return count

t=int(input())
for _ in range(t):
    n, m = map(int,input().split())

    visit=[False for i in range(n+1)]
    graph=[[] for i in range(n+1)]
    for i in range(m):
        a, b = list(map(int, input().split()))
        graph[a].append(b)
        graph[b].append(a)


    
    answer = dfs(1, visit, graph, 0)
    print(answer)