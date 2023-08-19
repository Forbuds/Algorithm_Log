import sys
input = sys.stdin.readline

# nlogn
n = int(input())
arr = [tuple(map(int, input().strip().split())) for _ in range(n)]
dp = [[0, 0, 0] for _ in range(n + 1)]
 # 개수, 시작가능, 끝시간
arr = sorted(arr, key = lambda x:(x[1],x[0]))
# print(n,arr)
# print('dd')
# dp[0] = [0,arr[0][0],arr[0][1]]
# 1~3
#   5~8
#   3~6
for i in range(n):
    # print(dp)
    # print(arr[i])
    # print(dp[i][1],arr[i][0],arr[i][1],dp[i][2])
    if dp[i][1]<= arr[i][0] and arr[i][1] <= dp[i][2] :#개꿀인 경우: dp[i][1]<= arr[i][0] or
        # print('꿀')
        if arr[i][0]==arr[i][1]:
            dp[i + 1] = (dp[i][0]+1, arr[i][1], arr[i][1])
        else:
            dp[i+1] = (dp[i][0],dp[i][1],arr[i][1])

    else: # 아닌 경우
        if dp[i][2] <= arr[i][0]:  # 회의 가능
            # print('+1')
            dp[i + 1] = (dp[i][0] +1,dp[i][2], arr[i][1])


        else:
            dp[i + 1] = (dp[i][0], dp[i][1], dp[i][2])


print(dp[-1][0])