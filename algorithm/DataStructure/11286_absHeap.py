import sys
import heapq
input =sys.stdin.readline



"""
if __name__=="__main__":
    t=int(input())

    heap=[[0,0]]
    for _ in range(t):
        num = int(input())

        # print(heap)
        
        if num==0:
            if len(heap)==1:
                print(0)
            
            else:
                heap[1], heap[-1] = heap[-1], heap[1]
                p = heap.pop()
                print(p[1])
                parent=1
                child=2
                while child<len(heap):
                    if child+1<len(heap) and heap[child][0]== heap[child+1][0]:
                        if heap[child][1]>heap[child+1][1]:
                            child+=1
                    elif child+1<len(heap) and heap[child][0]>heap[child+1][0]:
                        child+=1
                    
                    if heap[parent][0] == heap[child][0]:
                        if heap[parent][1]>heap[child][1]:
                            heap[parent], heap[child] = heap[child], heap[parent]
                    elif heap[parent][0]>heap[child][0]:
                        heap[parent], heap[child] = heap[child], heap[parent]
                    else:
                        break
                    parent=child
                    child*=2

        elif num!=0:
            heap.append([abs(num), num])

            idx = len(heap)-1
            while idx >1:
                if heap[idx][0]==heap[idx//2][0]:
                    if heap[idx][1]<heap[idx//2][1]:
                        heap[idx], heap[idx//2] = heap[idx//2], heap[idx]

                elif heap[idx][0]<heap[idx//2][0]:
                    heap[idx], heap[idx//2] = heap[idx//2], heap[idx]
                else:
                    break
                idx//=2
"""

if __name__=="__main__":

    t = int(input())

    heap=[]
    for _ in range(t):
        num = int(input())

        if num==0:
            if not heap:
                print(0)
            else:
                print(heapq.heappop(heap)[1])
        else:
            heapq.heappush(heap, [abs(num), num])