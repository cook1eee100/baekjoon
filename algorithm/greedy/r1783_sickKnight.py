import sys
input = sys.stdin.readline

n, m = map(int, input().split())


answer=0
if n==1:
    answer=1

elif n==2:
    answer=m//2 + m%2
    if answer>4:
        answer=4

elif n>=3:
    if m==1:
        answer=1
    elif m==2:
        answer=2
    elif m==3:
        answer=3
    elif m==4 or m==5 or m==6:
        answer=4
    elif m>=7:
        answer=m-2
print(answer)


"""
min() 활용

m>=3보다 큰경우 체크

n, m = map(int, input().split())
if n==1:
    print(1)
elif n==2:
    print(min(4, (m-1)//2+1))
else:
    if m<=6:
        print(min(4, m))
    else:
        print(m-2)

"""