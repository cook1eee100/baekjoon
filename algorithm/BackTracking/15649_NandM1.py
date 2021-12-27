import sys
input = sys.stdin.readline


"""
def dfs(s, n, m):
    if len(s)==m:
        print(s)
        return
    
    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            dfs(s, n, m)
            s.pop()


n,m = map(int, input().split())
s=[]

dfs(s, n, m)
"""




def dfs(depth, out, visit, n, m):
    if depth==m:
        print(" ".join(map(str, out)))
        return

    for i in range(0, n):
        if visit[i]==False:
           out.append(i+1)
           visit[i]=True
           dfs(depth+1, out, visit, n, m)
           out.pop()
           visit[i]=False


n, m = map(int, input().split())


visit=[False for _ in range(n)]
out=[]
depth=0
dfs(depth, out, visit, n, m)


