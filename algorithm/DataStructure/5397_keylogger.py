import sys
input = sys.stdin.readline



if __name__=="__main__":
    t = int(input())
    

    for _ in range(t):
        s= input().strip()
        left=[]
        right=[]
        for i in range(len(s)):
            if s[i]=="<":
                if left:
                    right.append(left.pop())
            elif s[i]==">":
                if right:
                    left.append(right.pop())

            elif s[i]=="-":
                if left:
                    left.pop()

            else:
                left.append(s[i])

        leftStr="".join(left)
        rightStr="".join(reversed(right))
        print(leftStr+rightStr)








"""

    cursor 를 값으로 체크하지 말고

    cursor 위치를 기준으로 왼쪽 list, 오른쪽 list 나눠서 생각해서

    커서가 옮겨지면 리스트에서 값 빼서 다른 리스트에 넣는 방식



#  내가 푼 문제 시간초과
if __name__=="__main__":
    t=int(input())

    for _ in range(t):
        s= input().strip()

        stack=[]
        answer=""
        c=0
        for i in range(len(s)):
            if s[i]=="<" or s[i]==">":
                stack.append(s[i])
            
            elif s[i]=="-":
                if c>0:
                    answer=answer[:c-1]+answer[c:]
                    c-=1
            else:
                while stack:
                    data=stack.pop()
                    if data == "<" and c>0:
                        c-=1
                    elif data ==">" and c<len(answer):
                        c+=1

                answer=answer[:c]+s[i]+answer[c:]
                c+=1
        print(answer)
"""





