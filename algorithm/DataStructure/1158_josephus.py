import sys
input = sys.stdin.readline

n, k = map(int, input().split())
graph=[i for i in range(1, n+1)]

answer=[]
count=1
idx=0
while graph:
    # print(count, idx)
    if count%k==0:
        # print('---------', count, idx)
        answer.append(str(graph.pop(idx)))
        idx-=1
        if not graph:
            break

    count+=1
    idx=(idx+1)%len(graph)

s=", ".join(answer)
print("<"+s+">")


"""
N,K = map(int,input().split())
arr = [i for i in range(1,N+1)]    # 맨 처음에 원에 앉아있는 사람들

answer = []   # 제거된 사람들을 넣을 배열
num = 0  # 제거될 사람의 인덱스 번호

for t in range(N):
    num += K-1  
    if num >= len(arr):   # 한바퀴를 돌고 그다음으로 돌아올때를 대비해 값을 나머지로 바꿈  
        num = num%len(arr)
 
    answer.append(str(arr.pop(num)))
print("<",", ".join(answer)[:],">", sep='')

"""