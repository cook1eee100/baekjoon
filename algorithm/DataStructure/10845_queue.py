import sys
input =sys.stdin.readline


def size(queue):
    return len(queue)

def empty(queue):
    if size(queue) ==0:
        return 1
    else:
        return 0

def front(queue):
    if empty(queue)==1:
        return -1
    return queue[0]

def back(queue):
    if empty(queue)==1:
        return -1
    return queue[-1]
    
def pop(queue):
    if empty(queue)==1:
        return -1
    return queue.pop(0)

def push(queue, num):
    queue.append(num)


n=int(input())
queue=[]

for _ in range(n):
    command = input().rstrip()

    l = len(command.split())

    if l ==1:
        if command=="front":
            print(front(queue))
        elif command=="back":
            print(back(queue))
        elif command=="empty":
            print(empty(queue))
        elif command=="size":
            print(size(queue))
        elif command=="pop":
            print(pop(queue))
        else:
            pass

    elif l==2:
        c, num = command.split()
        if c=="push":
            push(queue, int(num))

        else:
            pass