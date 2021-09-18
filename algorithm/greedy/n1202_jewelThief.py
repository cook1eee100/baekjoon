n, k = map(int, input().split())

jewelList=[]
for _ in range(n):
    m, v = list(map(int, input().split()))
    jewelList.append([v, m])

bagList=[]
for _ in range(k):
    c = int(input())
    bagList.append(c)

print(jewelList)
print(bagList)

