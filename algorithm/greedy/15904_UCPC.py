import sys
input = sys.stdin.readline

s = input()

ucpc=['U','C','P','C']
check=0
answer=''
for i in range(len(s)):
    if s[i] in ucpc[check]:
        answer+=s[i]
        check+=1
        if check==4:
            break

if answer=="UCPC":
    print("I love UCPC")
else:
    print("I hate UCPC")