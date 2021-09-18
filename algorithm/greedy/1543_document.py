s = input()
f = input()

answer=0    
i=0
while i < len(s)-len(f)+1:
    if s[i:i+len(f)] == f:
        answer+=1
        i+=len(f)
    else:
        i+=1
print(answer)