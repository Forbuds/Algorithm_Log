https://leetcode.com/problems/network-delay-time/description/

743. Network Delay Time : Medium

You are given a network of n nodes, labeled from 1 to n. 
You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), 
where ui is the source node, vi is the target node, 
and wi is the time it takes for a signal to travel from source to target.
We will send a signal from a given node k. 
Return the minimum time it takes for all the n nodes to receive the signal. 
If it is impossible for all the n nodes to receive the signal, return -1.

Example 1:

  Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
  Output: 2
Example 2:

  Input: times = [[1,2,1]], n = 2, k = 1
  Output: 1
Example 3:

  Input: times = [[1,2,1]], n = 2, k = 2
  Output: -1


Constraints:

  1 <= k <= n <= 100
  1 <= times.length <= 6000
  times[i].length == 3
  1 <= ui, vi <= n
  ui != vi
  0 <= wi <= 100
  All the pairs (ui, vi) are unique. (i.e., no multiple edges.)

class Solution:

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq as hq
        INF = int(1e9)
        distance = [INF]*(n+1)
        g = defaultdict(list)
        for a,b,c in times:
            g[a].append((b,c))


        def dijkstra(k):
            q = []
            hq.heappush(q,(0,k))
            distance[k] = 0
            while q:
                dist, node = hq.heappop(q)
                if distance[node] < dist:
                    continue
                for x in g[node]:
                    n_c, cost = x[0], x[1]
                    cost += dist
                    if cost < distance[n_c]:
                        distance[n_c] = cost
                        hq.heappush(q,(cost,n_c))



        dijkstra(k)

        result = max(distance[1:])
        return -1 if result == INF else result
