import sys
input =sys.stdin.readline


def dfs(depth, total, plus, minus, mul, div, graph):
    global minValue, maxValue
    if depth==len(graph):
        minValue=min(minValue, total)
        maxValue=max(maxValue, total)
        return

    if plus:
        dfs(depth+1, total+graph[depth], plus-1, minus, mul, div, graph)
    if minus:
        dfs(depth+1, total-graph[depth], plus, minus-1, mul, div, graph)
    if mul:
        dfs(depth+1, total*graph[depth], plus, minus, mul-1, div, graph)
    if div:
        dfs(depth+1, int(total/graph[depth]), plus, minus, mul, div-1, graph)



if __name__=="__main__":
    n=int(input())
    graph=list(map(int, input().split()))
    op = list(map(int, input().split()))

    minValue=1e9
    maxValue=-1e9
    dfs(1, graph[0], op[0], op[1], op[2], op[3], graph)
    print(maxValue)
    print(minValue)