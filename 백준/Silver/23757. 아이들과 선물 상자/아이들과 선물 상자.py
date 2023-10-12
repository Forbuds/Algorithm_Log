import sys
from heapq import heapify,heappop,heappush
input = sys.stdin.readline

n,m = map(int, input().strip().split())
present = list(map(lambda x: -1*int(x), input().strip().split()))
heapify(present)
ch = list(map(int, input().strip().split()))
flag = True
for x in ch:
    if abs(present[0])>= x:
        tmp = heappop(present)
        heappush(present, tmp+x)

    else:
        # print('실망')
        flag = False
if flag:
    print(1)
else:
    print(0)