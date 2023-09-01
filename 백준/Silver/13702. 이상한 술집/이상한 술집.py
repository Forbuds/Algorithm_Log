import sys

input = sys.stdin.readline

n,k = map(int,input().strip().split())
arr = [int(input().strip()) for _ in range(n)]
s = 1
e = max(arr)
while s<=e:
    result = 0
    mid = (s+e)//2
    for x in arr:
        if x >= mid:
            result += x//mid
    # print(s,mid,e,result)
    if result >= k:
        s = mid +1
        length = mid
    else:
        e = mid -1
print(length)