n=list(input())

sum=0
for i in n:
    sum+=int(i)

if sum%3!=0 or '0' not in n:
    print(-1)
else:
    n.sort(reverse=True)
    answer = "".join(n)
    print(answer)



"""
3의 배수는 각 자리의 수를 다 더한 값에 3으로 나누면 나머지가 0

30으로 안나누는 이유 : 30의 배수여도 각자리 수를 다 더했을때 30이하 임 그래서 3으로 나누서 체크하고 일의 자리에 들어갈 0이 있는지 없는지 체크
"""