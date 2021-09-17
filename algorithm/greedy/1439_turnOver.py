s = input()

answer=0
for i in range(1, len(s)):
    if s[0]!=s[i] and s[i-1]!=s[i]:
        answer+=1

print(answer)
    