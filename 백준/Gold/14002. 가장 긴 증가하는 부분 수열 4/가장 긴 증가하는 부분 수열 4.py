import sys
import copy
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().strip().split()))
dp = [[arr[i]] for i in range(n)]
def max_(a,b):
    if len(a) < len(b):
        return b
    else:
        return a

for i in range(1,n):
    for j in range(i):
        if arr[i] > arr[j]:
            tmp = copy.deepcopy(dp[j])
            tmp.extend([arr[i]])
            dp[i] = max_(dp[i], tmp)

len_list = [(len(x),x) for x in dp]
k,l = sorted(len_list)[-1]

print(k)
print(' '.join(map(str,l)))
