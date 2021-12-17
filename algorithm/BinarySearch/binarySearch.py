
a=[1,3,5,6,7,8,9,14,26,47,58]
n=int(input())



start=0
end=len(a)-1

while end>=start:
    mid=((start+end)//2)
    if a[mid]==n:
        print(mid)
        break
    
    elif a[mid]>n:
        end=mid-1

    else:
        start=mid+1
else:
    print("값 없음")


"""
1 3 5
"""