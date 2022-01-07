import sys
input = sys.stdin.readline


if __name__=="__main__":
    
    
    while True:
        s=input()
        if s==".\n":
            break

        check=True
        stack=[]
        for i in range(len(s)):
            if s[i]=="(" or s[i]=="[":
                stack.append(s[i])
            elif s[i]==")":
                if not stack:
                    check=False
                
                elif stack.pop()!="(":
                    check=False
            elif s[i]=="]":
                if not stack:
                    check=False
                
                elif stack.pop()!="[":
                    check=False

        if check and not stack:
            print("yes")
        else:
            print("no")

        
