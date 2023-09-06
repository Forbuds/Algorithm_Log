import sys
import heapq
input = sys.stdin.readline
h = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x==0:
        # 출력 및 제거
        if len(h)==0:
            print(0)
        else:
            abs_x, x  = heapq.heappop(h)
            print(x)
    #
    else:
        heapq.heappush(h,(abs(x),x))