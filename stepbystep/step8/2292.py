n = int(input())

if n==1:
    print(1)
    exit()
idx=1
result=1
count=0
while True:
    result = result+6*idx
    if result >n-1:
        print(count+2)
        break
    count+=1        
    idx+=1



# # 다른 사람 코드
# n = int(input())

# nums_pileup = 1  # 벌집의 개수, 1개부터 시작
# cnt = 1
# while n > nums_pileup :
#     nums_pileup += 6 * cnt  # 벌집이 6의 배수로 증가
#     cnt += 1  # 반복문을 반복하는 횟수
# print(cnt)