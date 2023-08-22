import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split()))
# 증가만 해도 돼 합도 커야 해
dp = [arr[i] for i in range(n)]
for i in range(1,n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[j]+arr[i], dp[i])
print(max(dp))