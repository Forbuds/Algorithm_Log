import sys
from heapq import heappush, heappop, heapify
input = sys.stdin.readline
t = int(input())
for i in range(t):
    k = int(input())
    pages = list(map(int, input().strip().split()))
    heapify(pages)
    result = 0
    while 1:
        if len(pages)<2:
            # if pages:
            #     result += heappop(pages)
            break
        else:
            n1 = heappop(pages)
            n2 = heappop(pages)
            num = n1 + n2
            result += num
            heappush(pages, num)
            # print(pages,result)
    print(result)