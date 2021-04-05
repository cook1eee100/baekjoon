n, x = map(int, input().split())

a = map(int, input().split())

for value in a:
    if value < x:
        print(value, end=" ")