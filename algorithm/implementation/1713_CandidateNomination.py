import sys
input = sys.stdin.readline



if __name__=="__main__":
    n=int(input())
    m=int(input())
    graph = list(map(int ,input().split()))

    canDict={}
    pri=0
    for i in graph:

        if i not in canDict.keys() and len(canDict.keys())<n:
            canDict[i]=[1, pri]
            pri+=1

        elif i in canDict.keys():
            canDict[i][0]+=1

        elif i not in canDict.keys() and len(canDict.keys())==n:
            temp = list(canDict.values())
            temp.sort()
            minValue = temp[0]
            
            for idx in canDict.keys():
                if canDict[idx]==minValue:
                    del canDict[idx]
                    canDict[i]=[1, pri]
                    pri+=1
                    break

    for i in sorted(list(canDict.keys())):
        print(i, end=" ")



    


"""
# 다른사람 코드
import sys
input = sys.stdin.readline

N = int(input())
W = int(input())
num = list(map(int, input().split(" ")))

photo = dict()
for i in range(W) :
    if num[i] in photo :
        photo[num[i]][0] += 1
    else : 
        if len(photo) < N :
            photo[num[i]] = [1, i]
        else :
            del_list = sorted(photo.items(), key= lambda x : (x[1][0] , x[1][1]) )
            del_key = del_list[0][0]
            del(photo[del_key])
            photo[num[i]] = [1, i]

ans_list = list(sorted(photo.keys()))
answer = str(ans_list[0])
for i in ans_list[1: ] :
    answer += " " + str(i)
print(answer)
"""
            

