# 풀긴 풀었는데 시간초과인듯?
import sys
input = sys.stdin.readline

s= list(input().strip())
m = int(input())

cursor=len(s)
for _ in range(m):
    command = input().strip()

    if len(command.split())==1:
        if command=='L':
            if cursor!=0:
                cursor-=1
        elif command=='D':
            if cursor!=len(s):
                cursor+=1
        elif command=='B':
            if cursor!=0:
                # print(len(s), cursor)
                s.pop(cursor-1)
                cursor-=1

    elif len(command.split())==2:
        c, x = command.split()
        if c=='P':
            s.insert(cursor, x)
            cursor+=1

print("".join(s))




"""
리스트 보다 문자열 슬라이싱이 더 빠름다고함 

****
2개의 스택으로 나눠서 cursor를 기준으로 2개의 스택에서 데이터를 주고받는 방법

import sys 
input = sys.stdin.readline

left_stack = list(input()[:-1]) 
right_stack = list() 
testcase = int(input()) 

for _ in range(testcase): 
    cmd = input() 
    if cmd[0] == 'L' and left_stack: 
        right_stack.append(left_stack.pop()) 

    elif cmd[0] == 'D' and right_stack: 
        left_stack.append(right_stack.pop()) 

    elif cmd[0] == 'B' and left_stack: 
        left_stack.pop()

    elif cmd[0] == 'P': 
        left_stack.append(cmd[2])

sys.stdout.write(''.join(left_stack + right_stack[::-1]))

"""





