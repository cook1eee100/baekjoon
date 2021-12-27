import sys
input = sys.stdin.readline

def dfs(depth, out, visit, n, m):
    if depth==m:
        print(" ".join(map(str, out)))
        return
    
    for i in range(n):
        if not out:
            out.append(i+1)
            visit[i]=True
            dfs(depth+1, out, visit, n, m)
            out.pop()
            visit[i]=False
        
        else:
            if visit[i]==False:
                if out[-1]<i+1:
                    out.append(i+1)
                    visit[i]=True
                    dfs(depth+1, out, visit, n, m)
                    out.pop()
                    visit[i]=False


n, m =map(int, input().split())
visit=[False for _ in range(n)]
out=[]

depth=0
dfs(depth, out, visit, n, m)