import sys
from collections import deque
input = sys.stdin.readline


def bfs(n, k):
    queue = deque()
    queue.append([n, 0])
    checkList=set([n])
    
    MAX = 10**5             # 메모리 초과 방지용
    while queue:
        n, count = queue.popleft()

        if n==k:
            return count

        for i in [n-1, n+1, n*2]:
            if 0<=i<=MAX and i not in checkList:
                queue.append([i, count+1])
                checkList.add(i)


n, k = map(int, input().split())

count=bfs(n, k)
print(count)



"""

"""