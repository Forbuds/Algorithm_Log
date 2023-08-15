import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*(11+1)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,11+1):

    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(n):
    target = int(input())
    print(dp[target])