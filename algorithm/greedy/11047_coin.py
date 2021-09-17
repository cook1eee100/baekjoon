n, k = map(int, input().split())

answer=0
coinList=[]
for _ in range(n):
    coinList.append(int(input()))

coinList.sort(reverse=True)

for i in range(len(coinList)):
    answer+=k//coinList[i]
    k=k%coinList[i]

print(answer)