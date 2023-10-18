import sys
input = sys.stdin.readline
n ,m = map(int,input().strip().split())
arr = list(map(int,input().strip().split()))

s,e = 0,1
cnt = 0
while s<=e and e<=n :
    # print(s,e)
    total =sum(arr[s:e])
    if total ==m:
        cnt +=1
        s+=1
    elif total < m:
        e +=1
    else:
        s +=1

print(cnt)