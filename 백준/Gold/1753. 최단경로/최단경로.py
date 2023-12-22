import sys
import heapq as hq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().strip().split())
graph = [[] for _ in range(n)]
result = [INF]*n
v = [False]*n
start = int(input())
start-= 1

for i in range(m):
    a, b, cost = map(int, input().strip().split())
    graph[a-1].append((b-1,cost))


q = []
hq.heappush(q,(0,start))
result[start] = 0
while q:
    dist, n_c =  hq.heappop(q)
    if result[n_c] < dist:
        continue
    for x in graph[n_c]:
        n_n, cost = x[0], x[1]
        cost += dist
        if cost < result[n_n]:
            result[n_n] = cost
            hq.heappush(q,(cost,n_n))

for i in range(n):
    if result[i] == INF:
        print('INF')
    else:
        print(result[i])