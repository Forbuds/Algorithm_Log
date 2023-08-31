import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split()))
m = int(input())

s = 1
e = max(arr)

while s<=e:
    mid = (s+e)//2
    total = 0
    for x in arr:
        total+= min(mid, x)
    # print(s,mid,e,total,m)
    if total > m:
        e = mid -1
    else:
        s = mid +1
print(e)