"""  내가 푼거
import sys
input=sys.stdin.readline

x, y = map(int, input().split())

rat=(y*100)//x

if rat>=99:
    end=-1

else:
    start=1
    end=x
    while start<end:
        mid=(start+end)//2

        rating=((y+mid)*100)//(x+mid)
        # print(rating, mid)
        
        if rat<rating:
            end=mid
        else:
            start=mid+1

print(end)


"""
import sys
input = sys.stdin.readline

x,y = map(int, input().split())
z=(y*100)//x
if z>=99:
    print(-1)
else:
    answer=0
    start=1
    end=x

    while start<=end:
        mid=(start+end)//2
        rating=((y+mid)*100)//(x+mid)

        if rating<=z:
            start=mid+1
        else:
            answer=mid
            end=mid-1

    print(answer)