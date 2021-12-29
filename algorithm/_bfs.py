from collections import deque

def bfs(v, graph, check):
    queue=deque()
    queue.append(v)
    check[v]=False
    while queue:
        num = queue.popleft()
        print(num, end=" ")

        for i in graph[num]:
            if check[i]:
                queue.append(i)
                check[i]=False