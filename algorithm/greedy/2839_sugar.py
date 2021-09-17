sugar = int(input())

answer=0

while sugar>=0:
    if sugar%5==0:
        answer+=sugar//5
        sugar=0
        break
    sugar-=3
    answer+=1

if sugar==0:
    print(sugar)
else:
    print(-1)
