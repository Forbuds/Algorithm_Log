import sys
from bisect import bisect_left
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().strip().split()))
q = [arr[0]]

for i in range(1,n):
    x = arr[i]
    if q[-1] < x:
        q.append(x)
    else:
        index = bisect_left(q,x)
        q[index] = x
print(n-len(q))