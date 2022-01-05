import sys
input = sys.stdin.readline



def dfs(depth, graph, total, add, minus, mul, div):
    global minValue
    global maxValue

    if depth==len(graph):
        if total<minValue:
            minValue=total

        if total>maxValue:
            maxValue=total
        return

    if add:
        dfs(depth+1, graph, total+graph[depth], add-1, minus, mul, div)
    if minus:
        dfs(depth+1, graph, total-graph[depth], add, minus-1, mul, div)
    if mul:
        dfs(depth+1, graph, total*graph[depth], add, minus, mul-1, div)
    if div:
        dfs(depth+1, graph, int(total/graph[depth]), add, minus, mul, div-1)

if __name__ == "__main__":
    n=int(input())
    graph=list(map(int,input().split()))
    op = list(map(int, input().split()))

    minValue=1e9
    maxValue=-1e9
    
    dfs(1, graph, graph[0], op[0], op[1], op[2], op[3])       # op로 받아서 if 문 쓸때 if op[0]:, if op[1]: 로 체크해도 될듯? 안되겟다 리스트라서
    print(maxValue)
    print(minValue)




"""
    ***** 문제좀 잘 읽자
    
    풀이 1. permutations 써서 op 순서 구한뒤 계산하는방법

    풀이 2. dfs 풀 때 마지막 단계에서 종합해서 계산하는게 아니라 재귀 할때마다 계산처리 해서 넘기기


# 내가 푼 코드  - 시간 초과
import sys
input = sys.stdin.readline


def dfs(oper, graph, visit, out, answer):
    if len(oper)==len(out):
        s=""
        total=graph[0]
        for i in range(len(out)):
            if out[i]=="+":
                total+=graph[i+1]
            if out[i]=="-":
                total-=graph[i+1]
            if out[i]=="*":
                total*=graph[i+1]
            if out[i]=="/":
                total=int(total/graph[i+1])
            s+=str(graph[i])+out[i]
        s+=str(graph[-1])
        # print(s, total)
        
        answer.append(total)
            
        return

    for i in range(len(oper)):
        if not visit[i]:
            out.append(oper[i])
            visit[i]=1
            dfs(oper, graph, visit, out, answer)
            out.pop()
            visit[i]=0

    return

n = int(input())
graph=list(map(int, input().split()))

operCount = list(map(int, input().split()))
oper = ['+']*operCount[0]+['-']*operCount[1]+['*']*operCount[2]+['/']*operCount[3]


answer=[]
out=[]
visit=[0]*len(oper)
dfs(oper, graph, visit, out, answer)
print(max(answer))
print(min(answer))
"""