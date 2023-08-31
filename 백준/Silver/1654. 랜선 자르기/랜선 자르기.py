# https://www.acmicpc.net/problem/1654
import sys
input = sys.stdin.readline
arr = []
k, n = map(int,input().strip().split())
for i in range(k):
    arr.append(int(input().strip()))
# print(k,n,arr)
s = 1
e = max(arr)
while s<=e:
    mid = (s+e)//2
    result = 0
    for x in arr:
        result += x//mid
    # print(s, mid, e, result)
    if result >= n:      #mid가 너무 작음
        s = mid +1
    else:
        e = mid -1

print(e)