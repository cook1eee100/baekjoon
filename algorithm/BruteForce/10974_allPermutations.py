import sys
input = sys.stdin.readline


def dfs(n, out):

    if len(out)==n:
        print(" ".join(list(map(str, out))))
        return

    for i in range(1, n+1):
        if i not in out:
            out.append(i)
            dfs(n, out)
            out.pop()

if __name__=="__main__":

    n=int(input())

    dfs(n, [])