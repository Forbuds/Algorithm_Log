import sys
from heapq import heappop,heappush,heapify
input = sys.stdin.readline

n,h,t = map(int, input().strip().split())
# 인구수, 키, 횟수제한

c = [-1*int(input()) for i in range(n)]
heapify(c)
flag = True
if h> abs(c[0]):
    print('YES')
    print(0)
else:

    for i in range(t):
        height = heappop(c)
        heappush(c, int(height/2) if height<-1 else height)

        if h > abs(c[0]):
            print('YES')
            print(i+1)
            flag = False
            break
    
    answer = abs(heappop(c))
    if h <= answer and flag:
        print('NO')
        print(answer)