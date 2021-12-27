import sys
input = sys.stdin.readline

def dfs(out, n, m):
    if len(out)==m:
        print(" ".join(map(str, out)))
        return

    for i in range(1, n+1):
        out.append(i)
        dfs(out, n, m)
        out.pop()

n, m = map(int, input().split())
out=[]

dfs(out, n, m)