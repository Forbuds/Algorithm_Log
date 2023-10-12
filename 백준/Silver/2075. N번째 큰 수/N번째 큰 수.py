import sys
from heapq import heappop, heappush, heapify
input = sys.stdin.readline
heap = []
n = int(input())
for i in range(n):
    numbers = map(int, input().split())
    for number in numbers:
        if len(heap)<n:
            heappush(heap,number)
        else:
            if heap[0]<number:
                heappop(heap)
                heappush(heap, number)
print(heap[0])