import sys
sys.setrecursionlimit(10**9)
from collections import deque
input = sys.stdin.readline


n,m,r = map(int,input().split())
# print(n,m,r)

visited = [0]*(n+1)
g = [[] for _ in range(n+1)]

cnt = 1
for _ in range(m):
    u,v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)


def bfs(visited,g,r):
    global cnt
    queue = deque()
    queue.append(r)
    visited[r] = cnt
    cnt+=1
    while queue:
        r_ = queue.popleft()
        for i in sorted(g[r_]):
            if visited[i]==0:
                queue.append(i)
                visited[i] = cnt
                cnt+=1
bfs(visited,g,r)
for i in visited[1:]:
    print(i)