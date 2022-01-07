import sys
input = sys.stdin.readline



if __name__=="__main__":
    s = input().strip()

    stack=[]
    total=0

    for i in range(len(s)):
        if s[i]=="(":
            stack.append(s[i])

        elif s[i]==")":
            if s[i-1]=="(":
                stack.pop()
                total+=len(stack)

            elif s[i-1]==")":
                stack.pop()
                total+=1

    print(total)




"""
( ( ) ( ( ) ) )
        _  _
 _   ___   __

    "(" 일 때 스택에 추가

    ")" 일때
        1) 이전 문자가 "(" 일 때 - 
        2) 이전 문자가 ")" 일 때 - 

"""