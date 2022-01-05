import sys
input = sys.stdin.readline


def dfs(prev, depth, n, sign, out, answer):

    if len(out)==n+1:
        s = "".join(list(map(str, out)))
        answer.append(s)
        return
    
    for i in range(10):
        if i not in out:
            if sign[depth]=="<" and prev<i:
                out.append(i)
                dfs(i, depth+1, n, sign, out, answer)
                out.pop()
            elif sign[depth]==">" and prev>i:
                out.append(i)
                dfs(i, depth+1, n, sign, out, answer)
                out.pop()
            
    return


if __name__=="__main__":

    n= int(input())
    sign=input().strip().split()

    # print(n, sign)
    answer=[]
    for i in range(10):
        dfs(i, 0, n, sign, [i], answer)
    print(answer[-1])
    print(answer[0])