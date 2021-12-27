import sys
input = sys.stdin.readline



def dfs(idx, s, out, visit):
    if len(out)==6:
        print(" ".join(map(str, out)))
        return

    for i in range(idx, len(s)):
        if visit[i]==False:
            out.append(s[i])
            visit[i]=True
            dfs(i+1, s, out, visit)
            out.pop()
            visit[i]=False


while True:
    temp = list(map(int, input().split()))

    k = temp[0]
    s = temp[1:]
    if k==0:
        break

    visit=[False for _ in range(k)]
    out=[]
    idx=0
    dfs(idx, s, out, visit)
    print()