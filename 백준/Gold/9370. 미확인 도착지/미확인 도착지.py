import sys
import heapq as hq
from collections import defaultdict
input = sys.stdin.readline

INF = int(1e9)
TC = int(input())

for tc in range(TC):
    graph = defaultdict(list)
    n,m,t = map(int, input().strip().split())
    s,g,h = map(int, input().strip().split())


    for _ in range(m):
        a,b,d = map(int, input().strip().split())
        graph[a].append((b,d))
        graph[b].append((a, d))

    def dijkstra(s,e):
        distance = [INF] * (n + 1)

        q = [(0,s)]
        distance[s] = 0
        while q:
            dist, node = hq.heappop(q)
            if distance[node] < dist:
                continue
            for n_c, cost in graph[node]:
                cost += dist
                if cost < distance[n_c] :
                    distance[n_c] = cost
                    hq.heappush(q,(cost, n_c))
        # print(e, distance)
        return distance[e]
    # s g h end
    # s h g end
    g_to_h = dijkstra(g, h)
    re1 = dijkstra(s,g) + g_to_h
    re2 = dijkstra(s,h) + g_to_h
    result = []

    for _ in range(t):
        end = int(input())
        now = dijkstra(s, end)
        # print(re1,re2,dijkstra(s,end))
        cal = min(re1 +dijkstra(h,end),re2 +dijkstra(g,end))
        if cal == now:
            result.append((end,cal))
    # print(result)
    print(' '.join(list(map(str,[n for n,x in sorted(result)]))))
