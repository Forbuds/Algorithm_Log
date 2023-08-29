import sys
from collections import deque

input = sys.stdin.readline

n,m,r = map(int, input().strip().split())
g = [[] for _ in range(n+1)]
v = [0]*(n+1)
for i in range(m):
    a,b = map(int, input().strip().split())
    g[a].append(b)
    g[b].append(a)
q = deque([])
def dfs(r):
    cnt = 1
    v[r] = 1
    q.append(r)
    cnt+=1
    while q:
        n_c = q.pop()
        if v[n_c] == 0:
            v[n_c] = cnt
            cnt+=1
        # print(g[n_c])
        for i in sorted(g[n_c]):
            if v[i]==0:
                q.append(i)



dfs(r)
print(*v[1:],sep='\n')
