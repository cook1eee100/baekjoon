n = int(input())
count=0

if n<100:
    print(n)
else:
    count+=99
    for idx in range(100, n+1):
        a = str(idx)
        if ((int(a[0])-int(a[1])) == (int(a[1])-int(a[2]))):
            count+=1
    print(count)

