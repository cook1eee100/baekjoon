import sys
input = sys.stdin.readline



if __name__=="__main__":
    s = list(input().strip())
    stack=[]
    print(s)


    for idx in s:
        if idx =="(" or idx=="[":
            stack.append(idx)
