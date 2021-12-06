string = input()

strList = string.split('.')

check=0
for i in range(len(strList)):
    s = strList[i]
    if len(s)%2!=0:
        check=1
        break

    elif len(s)%4==0:
        strList[i]='A'*len(s)
    else:
        strList[i]='A'*(len(s)//4)*4+'B'*2


if check==1:
    print(-1)

else:
    answer=".".join(strList)
    print(answer)
    