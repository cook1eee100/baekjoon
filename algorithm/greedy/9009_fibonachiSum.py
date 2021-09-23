import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    fiboList=[0,1]
    total=0
    while True:
        total=fiboList[-1]+fiboList[-2]
        if total<=n:
            fiboList.append(total)
        else:
            break
    fiboList.sort(reverse=True)
    
    answer=[]
    for i in fiboList:
        if n==0:
            break
        elif i <=n:
            answer.append(i)
            n=n-i
    answer.sort()

    for i in answer:
        print(i, end=" ")
    print()
        
    