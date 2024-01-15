# 루트가 1인 트리가 주어질 때, 각 노드의 부모를 구하는 문제
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
arr = [0]*(n+1)
e = [[] for _ in range(n+1)]
# 모든 노드를 방문하면서 트리를 그리자. dfs?bfs?
for i in range(n-1):
    a,b  = map(int, input().split())
    e[a].append(b)
    e[b].append(a)
def bfs(e,v):
    q = deque([v])
    visited = [False]*(n+1)
    visited[v] = True
    while q:
        x = q.popleft()
        for i in e[x]:
            if not visited[i]:
                arr[i] = x
                q.append(i)
                visited[i]= True


bfs(e,1)
for i in range(2,n+1):
    print(arr[i])