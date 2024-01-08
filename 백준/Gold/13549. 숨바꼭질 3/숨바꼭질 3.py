import sys
import collections
import heapq as hq
input = sys.stdin.readline
n,k = map(int,input().strip().split())
INF = int(1e9)
distance = [INF]*100001
distance[n] = 0
q = [(0,n)]
while q:
    dist,now = hq.heappop(q)
    if distance[now] < dist:
        continue
    for a,b in ((now+1,dist+1),(now-1,dist+1),(now*2,dist)):
        if 0<= a <= 100000 and distance[a]>b:
            distance[a] = b
            hq.heappush(q,(b,a))
print(distance[k])