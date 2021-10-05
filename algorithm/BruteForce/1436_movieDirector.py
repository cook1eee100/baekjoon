n = int(input())

num=666
cnt=0
while True:
    if '666' in str(num):
        cnt+=1
    
    if cnt == n:
        print(num)
        break
    num+=1



"""
문제 666이 들어가는 숫자들 중에서 순서찾기
666이 들어가는지 체크해서 
"""