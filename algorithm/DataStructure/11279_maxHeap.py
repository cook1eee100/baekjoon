import sys
import heapq
input = sys.stdin.readline




"""
if __name__=="__main__":
    n=int(input())

    heap=[0]
    for _ in range(n):
        num = int(input())
    

        if num==0:
            if len(heap)==1:
                print(0)
            else:
                heap[1], heap[len(heap)-1] = heap[len(heap)-1], heap[1]
                p = heap.pop()
                print(p)

                parent=1
                child=2

                while child<= len(heap)-1:
                    if child+1 <=len(heap)-1 and heap[child]<heap[child+1]:
                        child+=1
                    
                    if heap[parent]>heap[child]:
                        break
                    
                    heap[parent], heap[child] = heap[child], heap[parent]

                    parent=child
                    child*=2

        else:
            heap.append(num)
            i=len(heap)-1
            while i>1:
                if heap[i]>heap[i//2]:
                    heap[i], heap[i//2]= heap[i//2], heap[i]
                    i=i//2
                else:           # 애초에 넣을때 값 비교 해서 넣기때문
                    break
"""
    

# heapq 사용
if __name__=="__main__":
    n=int(input())
    heap=[]

    for _ in range(n):
        num=int(input())
        
        if num==0:
            if heap:
                print(heap)
                print("pop", heapq.heappop(heap))

            else:
                print("pop 0")
        else:
            heapq.heappush(heap, [-num, num])



"""
1
2 3
4 5 6 7
89 1011 1213 1415

"""