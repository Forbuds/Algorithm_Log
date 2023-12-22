import sys
import heapq as hq
input = sys.stdin.readline

n, e = map(int,input().strip().split())
g = [[] for _ in range(n)]
INF = int(1e9)

for _ in range(e):
    a,b, cost = map(int,input().strip().split())
    g[a-1].append((b-1,cost))
    g[b-1].append((a-1,cost))
a,b =     map(int,input().strip().split())
a,b = a-1,b-1

def dijkstra(start,end):
    distance = [INF]*n
    distance[start] = 0
    q = [(0,start)]
    while q:
        dist, n_c = hq.heappop(q)
        if distance[n_c] < dist:
            continue
        for node, cost in g[n_c]:
            cost += dist
            if cost < distance[node]:
                distance[node] = cost
                hq.heappush(q,(cost,node))
    return distance[end]

path1 = dijkstra(0,a) + dijkstra(a,b) + dijkstra(b,n-1)
path2 = dijkstra(0,b) + dijkstra(b,a) + dijkstra(a,n-1)

print(-1) if path1 >= INF or path2>=INF else print(min(path1,path2))
