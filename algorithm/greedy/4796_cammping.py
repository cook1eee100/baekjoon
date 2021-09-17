
i=1
while True:
    l, p, v = map(int, input().split())
    if l==0 or p ==0 or v==0:
        break

    day=0

    day+=(v//p)*l
    if v%p <=l:
        day+=(v%p)
    else:
        day+=l
    print(f"Case {i}: {day}")
    i+=1