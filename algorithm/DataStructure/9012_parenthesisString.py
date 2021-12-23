
import sys
input = sys.stdin.readline

t=int(input())
graph=[]
for _ in range(t):
    graph.append(input().strip())

for i in range(t):
    count=0
    for j in graph[i]:
        if j=="(":
            count+=1
        elif j==")":
            count-=1
            if count <0:
                break

    if count==0:
        print("YES")
    else:
        print("NO")
