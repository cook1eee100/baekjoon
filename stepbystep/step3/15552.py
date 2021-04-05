import sys

t = int(sys.stdin.readline())
inputList = []
for _ in range(t):
    inputList.append(map(int, sys.stdin.readline().split()))

for a, b in inputList:
    print(a+b)