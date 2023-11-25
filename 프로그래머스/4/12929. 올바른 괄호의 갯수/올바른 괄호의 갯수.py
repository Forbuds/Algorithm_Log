from collections import defaultdict
def solution(n):
    answer = 0
    # 카탈란 수 문제
    # c4 = c0*c3 + c1*c2 + c2*c1 + c3*c0
    dp = defaultdict(int)
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n+1):
        for j in range(0,i):
            dp[i] += dp[j] * dp[i-j-1]
    return dp[n]