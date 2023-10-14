# s시작, t 끝
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
n = int(input())
room = []
l = []
for i in range(n):
    l.append(list(map(int, input().strip().split())))
l = sorted(l,key = lambda x: x[0])
result = 1
heappush(room, l[0][1])
for i in range(1,n):
    s,t = l[i]
    if room[0] > s:
        heappush(room,t)
        result +=1
    else:
        heappop(room)
        heappush(room,t)
print(result)