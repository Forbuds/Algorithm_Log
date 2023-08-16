import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split()))
arr.sort()
m = int(input())
targets = list(map(int, input().strip().split()))

dp ={}
for i in arr:
    dp[i] = dp.get(i,0)+1
for i in targets:
    print(dp.get(i,0),end=' ')