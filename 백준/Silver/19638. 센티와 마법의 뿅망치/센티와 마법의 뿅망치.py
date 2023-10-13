import sys
from heapq import heappop,heappush,heapify, heapreplace
input = sys.stdin.readline

n,h,t = map(int, input().strip().split())
# 인구수, 키, 횟수제한

c = [-1*int(input()) for i in range(n)]
heapify(c)
cnt = 0
for i in range(t):
    if -c[0] == 1 or -c[0] < h:
        break
    else:
        heapreplace(c, -int(-c[0]//2))
        cnt+=1

if h > -c[0]:
    print('YES')
    print(cnt)
else:
    print('NO')
    print(-c[0])