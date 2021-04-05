t = int(input())

inputList=[]
for _ in range(t):
    inputList.append(map(int, input().split()))

for idx, [a, b] in enumerate(inputList):
    print(f"Case #{idx+1}: {a} + {b} = {a+b}")