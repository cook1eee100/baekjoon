import sys
input = sys.stdin.readline

if __name__=="__main__":
    s = list(input().strip())
    stack=[]
    answer=0
    tmp=1
    
    for idx in range(len(s)):
        if s[idx]=="(":
            stack.append(s[idx])
            tmp*=2
        elif s[idx]=="[":
            stack.append(s[idx])
            tmp*=3
        elif s[idx]==")":
            if not stack or stack[-1]=="[":
                answer=0
                break
            if s[idx-1]=="(":
                answer+=tmp
            stack.pop()
            tmp//=2

        elif s[idx]=="]":
            if not stack or stack[-1]=="(":
                answer=0
                break
            if s[idx-1]=="[":
                answer+=tmp
            stack.pop()
            tmp//=3
    
    if stack:
        print(0)
    else:
        print(answer)
            



"""
( ( ( ( ( )))))
2 2 2 2 2 
2 4 8 16 32



[ ( ( [ ]))]
3 2 2 3


[ ( ) ( )]
3 2   2
3 6 
    6


a*(b+b) = ab + ab 특징이용
(,[ 나오면 수를 곱하고 (), [] 완성이 될때 더하고 (,] 나오면 수를 나눔
"""