import sys
from collections import deque
input = sys.stdin.readline
n,m,r = map(int, input().strip().split())
g = [[] for i in range(n+1)]
v = [0]*(n+1)
for _ in range(m):
    a,b = map(int, input().strip().split())
    g[a].append(b)
    g[b].append(a)
q = deque([])
def bfs(r):
    q.append(r)
    cnt = 1
    v[r] = cnt
    cnt+=1
    while q:
        n_c = q.popleft()
        for x in sorted(g[n_c],key=lambda x:-x):
            if v[x] ==0:
                q.append(x)
                v[x] = cnt
                cnt += 1

bfs(r)
print(*v[1:],sep='\n')