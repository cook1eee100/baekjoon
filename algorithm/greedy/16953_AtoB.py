a, b = map(int, input().split())

answer=1
while b>a:
    if b%2==0:
        b=b//2
        answer+=1
    else:
        if b%10==1:
            b=b//10
            answer+=1
        else:
            break
if a==b:    
    print(answer)
else:
    print(-1)

