import sys
input = sys.stdin.readline

# 200000000
# 1500000->nlogn

n = int(input())

a = [tuple(map(int,input().strip().split())) for _ in range(n)]
dp = [0]*(n)


for i in range(n):
    dp[i] = max(dp[i],dp[i-1])
    fin = i + a[i][0] -1   # 오늘 일 채책한다면
    if fin < n:  # 일정 내에 일 끝내기 가능
        dp[fin] = max(dp[fin],dp[i-1]+a[i][1])

print(max(dp))