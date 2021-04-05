t = int(input())

inputList = []
for _ in range(t):
    inputList.append(map(int, input().split()))

for a, b in inputList:
    print(a+b)
    