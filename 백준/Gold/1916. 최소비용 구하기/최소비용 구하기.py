import sys
import collections
import heapq as hq
input = sys.stdin.readline
n = int(input())
m = int(input())
INF = int(1e9)
distance = [INF]*(n+1)
graph = collections.defaultdict(list)
for _ in range(m):
    s,e,cost = map(int, input().strip().split())
    graph[s].append((e,cost))
start, end = map(int, input().strip().split())

q = [(0,start)]
distance[start] = 0
while q:
    dist, now = hq.heappop(q)
    if distance[now] < dist:
        continue
    for x in graph[now]:
        node, cost = x[0],x[1]
        cost += dist
        if cost < distance[node]:
            distance[node] = cost
            hq.heappush(q,(cost,node))

print(distance[end])