s = int(input())

for _ in range(s):
    r, p = input().split()
    r = int(r)
    for idx in range(len(p)):
        print(p[idx]*r, end="")
    print()
