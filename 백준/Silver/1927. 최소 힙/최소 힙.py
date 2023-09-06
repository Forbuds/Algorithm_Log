import sys
import heapq
input = sys.stdin.readline
n = int(input())
h = []
for _ in range(n):
    x = int(input())
    if x==0:
        # 작은 값 출력 및 제거
        if len(h) == 0:
            print(0)
        else:
            print(heapq.heappop(h))
    else:
        heapq.heappush(h,x)