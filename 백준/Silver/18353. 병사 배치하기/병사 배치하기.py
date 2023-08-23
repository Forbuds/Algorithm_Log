import sys
from bisect import bisect_left
# bisect은 항상 오름차순일때만 사용하자
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().strip().split()))
arr.reverse()
q = []
q.append(arr[0])
for i in range(1,n):
    x = arr[i]
    # print(x)
    if q[-1] < x:
        q.append(x)
        # print('크다!',q)
    else:
        # print('--------------안크네!',q)
        idx = bisect_left(q,x)
        q[idx] = x
        # print('바꿨어', q)
# print(q)
print(n-len(q))