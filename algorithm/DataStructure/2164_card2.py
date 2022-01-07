import sys
from collections import deque
input = sys.stdin.readline





if __name__=="__main__":
    n=int(input())
    graph=deque()
    
    for i in range(1, n+1):
        graph.append(i)

    check=True
    while len(graph)!=1:
        if check:
            graph.popleft()
            check=False
        if not check:
            graph.append(graph.popleft())
            check=True
    
    """
    # 다른사람 코드
    while len(graph)>1:
        graph.popleft()
        graph.append(graph.popleft())

    """

    print(graph[0])