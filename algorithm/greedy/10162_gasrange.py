answer=[]
t = int(input())

sList = [300, 60, 10]

for i in sList:
    answer.append(t//i)
    t=t%i

if t!=0:
    print(-1)
else:
    for i in answer:
        print(i, end=" ")
