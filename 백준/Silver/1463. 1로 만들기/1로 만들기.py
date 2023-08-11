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
        arr = []
        if i%2==0:
            arr.append(dp[i//2])
        if i%3==0:
            arr.append(dp[i//3])
        arr.append(dp[i-1])
        # print(i, arr)
        dp[i] = min(arr)+1

    # print(dp)
    print(dp[n])

