import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline



n,m,r = map(int,input().split())

visited = [0]*(n+1)
g = [[] for i in range(n+1)]
cnt = 1
for _ in range(m):
    u,v = map(int,input().split())
    g[u].append(v)
    g[v].append(u)

def dfs(visited,g,r):
    global cnt
    visited[r]=cnt
    cnt+=1
    for r_ in sorted(g[r],reverse=True):
        if visited[r_]==0:
            dfs(visited,g,r_)

dfs(visited,g,r)
for i in visited[1:]:
    print(i)

