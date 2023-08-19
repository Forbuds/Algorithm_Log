import sys
input = sys.stdin.readline
#nlogn이 필요함

n,m = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
dp = [0]*(n+1)
dp[1] = arr[0]
for i in range(2,n+1):
    dp[i] = dp[i-1]+arr[i-1]
# print(dp)
for _ in range(m):
    i,j = map(int,input().strip().split())
    if i==j:
        print(dp[i]-dp[i-1])
    else:
        print(dp[j]-dp[i-1])