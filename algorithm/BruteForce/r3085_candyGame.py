import sys
input = sys.stdin.readline


def check(graph):
    maxValue=0
    for i in range(len(graph)):
        count=1
        for j in range(len(graph)-1):   # 가로 길이 체크
            if graph[i][j] == graph[i][j+1]:
                count+=1
            else:
                count=1

            if maxValue<count:
                maxValue=count

        count=1
        for j in range(len(graph)-1):   # 세로 길이 체크
            if graph[j][i] == graph[j+1][i]:
                count+=1
            else:
                count=1
            
            if maxValue<count:
                maxValue=count
    
    return maxValue


n = int(input())
graph = [list(input().strip()) for _ in range(n)]

answer=0
for i in range(n):
    for j in range(n-1):        # 오른쪽값과 체인지
        graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]
        temp = check(graph)
        graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]

        if temp>answer:
            answer=temp

    for j in range(n-1):        # 아래쪽값과 체인지
        graph[j][i], graph[j+1][i] = graph[j+1][i], graph[j][i]
        temp = check(graph)
        graph[j][i], graph[j+1][i] = graph[j+1][i], graph[j][i]

        if temp>answer:
            answer=temp

print(answer)




"""
1. 가로, 세로 최대길이 체크

2. 값 교체 방법

"""