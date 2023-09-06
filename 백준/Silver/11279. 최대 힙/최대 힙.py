import sys
import heapq
input = sys.stdin.readline
n = int(input())
h = []
for _ in range(n):
    x = int(input())
    if x==0:
        if len(h)==0:
            print(0)
        else:
            # 최대 힙
            a = -1 * heapq.heappop(h)
            print(a)
    else:
        heapq.heappush(h,-1*x)
        # 추가