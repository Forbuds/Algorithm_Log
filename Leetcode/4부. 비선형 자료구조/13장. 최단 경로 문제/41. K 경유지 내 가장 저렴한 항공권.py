https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

787. Cheapest Flights Within K Stops : Medium

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        import heapq as hq
        g = defaultdict(list)
        for f,t,p in flights:
            g[f].append((t,p))
        INF = int(1e9)
        distance = [(INF,INF)]*(n)
        # 경유지 몇 개 가는  중에, 

        def dij(src):
            q = [(0,0,src)]   # cost, 경유지 몇 개 ,node

            while q:
                cost, k, node = hq.heappop(q)
                if node == dst:
                    return cost
                if k < distance[node][1]:          # 이 줄과 바로 아래 두 줄은, https://8iggy.tistory.com/115에서와 같이 해당 노드에 방문하기 전보다 경유지가 적어야 한다. - 경유지가 적어야 방문.
                    distance[node] = (cost, k+1)   #아래에 넣어야 하는줄 알았더니(n_c) node에 해당되는 거였다. 사실 distance가 아니라 visited로 작성해도 됨
                    if k <= K:
                        for n_c, dist in g[node]:
                            dist += cost
                            hq.heappush(q,(dist, k+1,n_c))
            return -1
        result = dij(src)
        return result
