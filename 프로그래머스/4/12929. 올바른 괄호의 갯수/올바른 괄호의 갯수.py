from collections import defaultdict
def solution(n):
    dp = defaultdict(int)
    dp[0] = 1
    dp[1] = 1
    if n > 1:
        for k in range(2,n+1):
            for i in range(k):
                dp[k] += dp[i]*dp[k-i-1]
            
    return dp[n]
    
    
'''
    예시) N=4 (괄호 4쌍)
    4보다 작은 괄호 개수에 따른 정답을 dp로 생성 --> 0쌍은 1가지로 정의
    dp = [1, 1, 2, 5]

    경우 1) ( 한개도 없음 ) x 3쌍 가짓수 ----- dp[0] * dp[3] = 1x5
    경우 2) ( 1쌍 가짓수 ) x 2쌍 가짓수 ----- dp[1] * dp[2] = 1x2
    경우 3) ( 2쌍 가짓수 ) x 1쌍 가짓수 ----- dp[2] * dp[1] = 2x1
    경우 4) ( 3쌍 가짓수 ) x 0쌍 가짓수 ---- dp[3] * dp[0] = 5x1

     ∴ dp[4] = 5 +2 +2 +5 = 14
 
 '''