import sys
input = sys.stdin.readline


def dfs(s, out, n, m):
    if len(out) == m:
        print(" ".join(map(str, out)))
        return
    
    for i in range(s, n+1):
        out.append(i)
        dfs(i, out, n, m)
        out.pop()

n, m = map(int, input().split())
out=[]

s=1
dfs(s, out, n, m)