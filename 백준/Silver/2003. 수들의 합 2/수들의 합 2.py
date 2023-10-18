import sys
input = sys.stdin.readline
n ,m = map(int,input().strip().split())
arr = list(map(int,input().strip().split()))

s,e = 0,1
cnt = 0
while s<=e:
    # print(s,e)
    if e!=n:
        if sum(arr[s:e]) < m:
            e +=1
        elif sum(arr[s:e]) == m:
            cnt +=1
            s+=1
        else:
            s +=1
    else:
        if sum(arr[s:e]) == m:
            cnt += 1
            s += 1
        else:
            s +=1
print(cnt)