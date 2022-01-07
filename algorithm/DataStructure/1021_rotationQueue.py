import sys
from collections import deque
input = sys.stdin.readline




if __name__=="__main__":
    n, m = map(int, input().split())
    queue=deque()
    for i in range(1, n+1):
        queue.append(i)
    graph=list(map(int ,input().split()))

    answer=[]
    idx=0
    count=0
    while answer!=graph:

        if queue[0] == graph[idx]:
            answer.append(queue.popleft())
            idx+=1
        
        elif queue.index(graph[idx])<=len(queue)//2:
            queue.append(queue.popleft())
            count+=1
            """
            while graph[idx]!=queue[0]:
                queue.append(queue.popleft())
                count+=1
            """


        elif queue.index(graph[idx])>len(queue)//2:
            queue.insert(0, queue.pop())
            count+=1
            """
            while graph[idx]!=queue[0]:
                queue.appendleft(queue.pop())
                count+=1
            """
    print(count)






"""
1 2 3 4
0 1 2 3 

1 2 3 4 5
0 1 2 3 4 

"""