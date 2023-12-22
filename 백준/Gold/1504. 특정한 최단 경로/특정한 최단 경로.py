import sys
import heapq as hq
from collections import defaultdict
input = sys.stdin.readline

n, e = map(int,input().strip().split())
g = defaultdict(lambda: defaultdict(dict))
INF = int(1e9)

for _ in range(e):
    a,b, cost = map(int,input().strip().split())
    g[a-1][b-1] = cost
    g[b-1][a-1] = cost
a,b =     map(int,input().strip().split())
a,b = a-1,b-1
def solution():
    def dijkstra(start):
        distance = [INF]*n
        distance[start] = 0
        q = [(0,start)]
        while q:
            dist, n_c = hq.heappop(q)
            if distance[n_c] < dist:
                continue
            for node, cost in g[n_c].items():
                cost += dist
                if cost < distance[node]:
                    distance[node] = cost
                    hq.heappush(q,(cost,node))
        return distance

    from_start = dijkstra(0)
    if from_start[a]>= INF or from_start[b]>=INF:
        return -1
    from_a = dijkstra(a)
    if from_a[b]>= INF or from_a[n-1]>= INF:
        return -1
    from_b = dijkstra(b)
    if from_b[a]>= INF or from_b[n-1]>= INF:
        return -1
    path1 = from_start[a] + from_a[b] + from_b[n-1]
    path2 = from_start[b] + from_b[a] + from_a[n-1]
    result = min(path1,path2)
    if result >= INF:
        return -1
    else:return result


print(solution())