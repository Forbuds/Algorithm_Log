import sys

input = sys.stdin.readline

n,k = map(int,input().strip().split())
arr = list(map(int,input().strip().split()))

s = 1
e = max(arr)
result = 0
while s<=e:
    mid = (s+e)//2
    total =0
    for x in arr:
        total += x//mid

    if total >= n:
        s = mid +1
        result = mid
    else:
        e = mid -1
print(result)