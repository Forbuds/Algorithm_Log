import sys
from heapq import heappush, heappop
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    heappush(arr, int(input()))
result = 0
for i in range(n-1):
    tmp = heappop(arr) + heappop(arr)
    result += tmp
    heappush(arr,tmp)
    # print(result, arr)
print(result)