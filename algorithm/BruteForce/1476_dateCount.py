import sys
input = sys.stdin.readline

e, s, m= map(int, input().split())
value=[1, 1, 1]
year=1
while True:
    if value==[e,s,m]:
        print(year)
        break

    else:
        value[0]+=1
        value[1]+=1
        value[2]+=1
        year+=1
        if value[0]==16:
            value[0]=1
        if value[1]==29:
            value[1]=1
        if value[2]==20:
            value[2]=1