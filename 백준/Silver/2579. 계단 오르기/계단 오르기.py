# 세개의 계단이 있다면, 한 번 두번
# 두번 한번
# 근데 이미 두번 밟았다면 안됨
#
# 한칸전에 있는 애에서 하나 지나오기
#     올 수 있거나
#     아니거나(지나침)
# 두칸전에 있는 친구에서 한 번 지나오기

import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

if n==1:
    print(arr[1-1])
elif n==2:
    print(sum(arr))
else:
    dp = {}
    dp[1] = [(1,1,arr[1-1])]  # flag, 지금까지의 합
    dp[2] = [(1,2,arr[2-1]), (2,1,arr[1-1]+arr[2-1])]
    # dp[3] = [dp[1]에서, 2를 달고 지나오기 ] / dp2에서 1일 경우에만 1달고 지나오기
    # dp[4] = [dp[2]에서 ,2를 달고 지나오기] / [dp3이 2일 경우에만 1달고 지나오기]

    # print(n, arr, dp)

    for i in range(3,n+1):
        dp[i] = []
        for x,flag,sum_ in dp[i-1]:
            if flag ==2:
                dp[i].append((x+1,1,sum_+arr[i-1]))
        x,flag,sum_ = sorted(dp[i-2], key=lambda x:x[2])[-1]
        dp[i].append((x+1,2,sum_+arr[i-1]))

    # print(dp)
    print(sorted(dp[n], key=lambda x: x[2])[-1][2])