class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = defaultdict(list)
        for f,t,p in flights:
            g[f].append((t,p))
        q = [(0,src,k)]
        while q:
            cost, node, tmp = heapq.heappop(q)
            if node == dst:
                return cost
            if tmp >= 0:
                for n_c, dist in g[node]:
                    heapq.heappush(q,(cost+dist, n_c, tmp-1))
        return -1
      
