n = int(input())
a = n
count=0

while True:
    b=(a//10+a%10)%10
    a=(a%10)*10+b
    count+=1
    if a==n:
        break

print(count)