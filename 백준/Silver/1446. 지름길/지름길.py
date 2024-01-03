import sys
import heapq as hq
import collections
input = sys.stdin.readline
n, d = map(int, input().strip().split())
graph = collections.defaultdict(list)
INF = int(1e9)
distance = [INF]*(d+1)

for i in range(d):
    graph[i].append((i+1,1))
# print(len(graph))
for _ in range(n):
    a,b,cost = map(int, input().strip().split())
    if b>d:
        continue
    graph[a].append((b,cost))

q = [(0,0)]
distance[0] = 0
while q:
    dist, node = hq.heappop(q)
    if dist > distance[node]:
        continue
    for x in graph[node]:
        n_c, tmp_dist = x[0],x[1]
        # print(n_c, len(distance))
        # print(n_c,len(distance),distance[n_c])
        tmp_dist += dist
        if tmp_dist < distance[n_c]:
            distance[n_c] = tmp_dist
            hq.heappush(q,(tmp_dist , n_c))
print(distance[d])