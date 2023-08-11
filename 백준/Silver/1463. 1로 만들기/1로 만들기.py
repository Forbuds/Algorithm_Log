# DP 기억 안나서 다시

# 2의 배수인 친구
# 3의 배수인 친구
# 1뺀친구
# 중에 최소값 취하자

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())

if n==2 or n==3:
    print(1)
elif n==1:
    print(0)
else:

    dp = [0]*(n+1)


    dp[2] = 1
    dp[3] = 1


    for i in range(4,n+1):
        dp[i] = dp[i-1] + 1  # append연산이 오래 걸리니까 min을 취해주는 형식으로 변경
        if i%2==0:
            dp[i] = min(dp[i//2]+1, dp[i])
        if i%3==0:
            dp[i] = min(dp[i//3]+1, dp[i])

    # print(dp)
    print(dp[n])

