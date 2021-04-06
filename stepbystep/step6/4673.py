numberList = list(range(1, 10001))

for idx in range(1, 10001):
    a=str(idx)
    total=idx
    for i in range(len(a)):
        total+=int(a[i])

    if total>10000:
        pass
    else:
        numberList[total-1]=0


[print(i) for i in numberList if i not in [0]]
