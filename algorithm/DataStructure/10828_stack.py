import sys
input = sys.stdin.readline


def pop(stack):
    if empty(stack)==1:
        return -1
    return stack.pop()

def size(stack):
    return len(stack)

def empty(stack):
    if size(stack)==0:
        return 1
    return 0

def top(stack):
    if empty(stack)==1:
        return -1
    return stack[-1]

def push(stack, num):
    stack.append(num)


n=int(input())
stack=[]

for _ in range(n):
    command = input().strip()

    l = len(command.split())
    if l==1:
        if command == "pop":
            print(pop(stack))
        elif command == "size":
            print(size(stack))
        elif command == "empty":
            print(empty(stack))
        elif command == "top":
            print(top(stack))
        else:
            pass

    elif l==2:
        c, num = command.split()
        if c == "push":
            push(stack, int(num))
        else:
            pass