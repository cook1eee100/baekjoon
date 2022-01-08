import sys
import heapq
input = sys.stdin.readline


if __name__=="__main__":
    t = int(input())

    heap=[0]
    for _ in range(t):
        num=int(input())

        if num==0:
            if len(heap)==1:
                print(0)
            else:
                heap[1], heap[-1] = heap[-1], heap[1]
                p=heap.pop()
                print(p)

                parent=1
                child=2
                while child<=len(heap)-1:
                    if child+1<=len(heap)-1 and heap[child]>heap[child+1]:
                        child+=1

                    if heap[parent]>heap[child]:
                        heap[parent], heap[child] = heap[child], heap[parent]
                    parent=child
                    child*=2

        else:
            heap.append(num)

            idx = len(heap)-1

            while idx>1:
                if heap[idx]<heap[idx//2]:
                    heap[idx], heap[idx//2] = heap[idx//2], heap[idx]

                idx=idx//2



""" 
# heapq 사용
if __name__=="__main__":
    t = int(input())
    
    heap=[]
    for _ in range(t):
        num = int(input())

        if num==0:
            if not heap:
                print("pop", 0)
            else:
                print("pop", heapq.heappop(heap))

        else:
            heapq.heappush(heap, num)

"""