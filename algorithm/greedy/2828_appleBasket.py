n, m = map(int, input().split())
j=int(input())

appleList=[]
for _ in range(j):
    appleList.append(int(input()))


answer=0
l=1
r=m
for i in appleList:
    if l<=i<=r:
        continue

    elif i<l:
        answer+=l-i
        r-=(l-i)
        l=i

    elif i>r:
        answer+=i-r
        l+=i-r
        r=i
print(answer)