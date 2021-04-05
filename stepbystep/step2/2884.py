h, m = map(int, input().split())

if m<45:
    m+=60-45
    h-=1
    if h<0:
        h+=24
else:
    m-=45

print(h, m)
