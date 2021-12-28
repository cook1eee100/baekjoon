import sys
input = sys.stdin.readline

def dfs(n, m, graph, out):
    if len(out)==m:
        print(" ".join(map(str, out)))
        return

    for i in range(n):
        if graph[i] not in out:
            out.append(graph[i])
            dfs(n, m, graph, out)
            out.pop()


n, m =map(int, input().split())
graph = list(map(int, input().split()))
graph.sort()

out=[]
dfs(n, m, graph, out)