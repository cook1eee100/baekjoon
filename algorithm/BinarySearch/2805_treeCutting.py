import sys
input = sys.stdin.readline

n, m = map(int,input().split())
graph= list(map(int, input().split()))
graph.sort()

start=1
end=graph[-1]
answer=0
while start<=end:
    mid=(start+end)//2
    log=0
    for i in range(len(graph)-1, -1, -1):
        if graph[i]<=mid:
            break
        elif graph[i] >mid:
            log+=graph[i]-mid
    

    if log<m:
        end = mid-1
    elif log>=m:
        answer=mid
        start=mid+1

print(answer)