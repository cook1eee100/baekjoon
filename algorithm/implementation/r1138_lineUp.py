import sys
input = sys.stdin.readline

n=int(input())
graph=list(map(int, input().split()))

answer=[0]*n
for i in range(n):
    count=0
    maxCount=0
    for j in range(n):
    
        if graph[i]<=count and answer[j]==0:
            answer[j]=i+1
            break
        
        if answer[j]==0:
            count+=1


for i in answer:
    print(i, end=" ")




"""
    작은 수부터 
    왼쪽에 자기보다 큰 값이 있다고 생각하고 빈칸 만들어놓고 채워넣기
"""