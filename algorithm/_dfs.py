def dfs(v, graph, check):
    print(v, end=" ")
    check[v]=True
    
    for i in graph[v]:
        if not check[i]:
            dfs(i, graph, check)
