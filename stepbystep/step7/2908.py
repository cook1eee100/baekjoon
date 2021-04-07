num = input().split()

for idx in range(len(num)):
    num[idx]=list(num[idx])
    num[idx][0], num[idx][2] = num[idx][2], num[idx][0]
    num[idx]=''.join(num[idx])

print(max(num))