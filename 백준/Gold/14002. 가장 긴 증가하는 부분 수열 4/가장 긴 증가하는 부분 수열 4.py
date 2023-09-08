import sys
import copy
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().strip().split()))
dp = [1 for i in range(n)]
def max_(a,b):
    if len(a) < len(b):
        return b
    else:
        return a

for i in range(1,n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
k = max(dp)
print(k)
result  = []
for i in range(n-1,-1,-1):
    if dp[i] == k:
        result.append(arr[i])
        k-=1
print(*sorted(result))