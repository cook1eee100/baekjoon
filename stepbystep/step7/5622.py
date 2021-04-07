s = input()

dialList = ['ABC', 'DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
total=0

for idx1 in range(len(s)):
    for idx2 in range(len(dialList)):
        if s[idx1] in dialList[idx2]:
            total += idx2+2
            break
print(total+len(s))