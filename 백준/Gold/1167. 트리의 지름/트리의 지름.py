# 루트가 1인 트리가 주어질 때, 각 노드의 부모를 구하는 문제
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
result = []
g = [[] for _ in range(n+1)]
for _ in range(n):
    # 번호, 간선 정보 두 개씩 - 번호랑 정점까지의 거리
    # 두개씩 끊어서 받는다.
    tmp = list(map(int, input().rstrip().split()))
    v = tmp[0]
    tmp = tmp[1:-1]
    for i in range(len(tmp)//2):
        g[v].append((tmp[2*i],tmp[2*i+1]))

def bfs(s):
    q = deque([(s,0)])
    visited = [-1]*(n+1)
    visited[s] = 0
    result = [0,0]
    while q:
        node_cnt, cost_cnt = q.popleft()
        for node_nxt, cost_nxt in g[node_cnt]:
            if visited[node_nxt] == -1:
                cost_nxt += cost_cnt
                q.append((node_nxt,cost_nxt))
                visited[node_nxt] = cost_nxt
                if result[1]<cost_nxt:
                    result = [node_nxt,cost_nxt]
    return result

node, cost = bfs(1)
print(bfs(node)[1])