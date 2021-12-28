import sys
input = sys.stdin.readline



def dfs(s, n, m, graph, out):

    if len(out)==m:
        print(" ".join(map(str, out)))
        return
        
    for i in range(s, n):
        if graph[i] not in out:
            out.append(graph[i])
            dfs(i+1, n, m, graph, out)
            out.pop()


n, m = map(int, input().split())
graph = list(map(int, input().split()))
graph.sort()

out=[]
dfs(0, n, m, graph, out)
