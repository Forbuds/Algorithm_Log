import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


n,m,r = map(int,input().split())
g = [[] for i in range(n+1)]
visited =[0]*(n+1)
for i in range(m):
    u,v = map(int,input().split())
    g[u].append(v)
    g[v].append(u)
cnt = 1
def dfs(visited,s,g):
    global cnt
    visited[s] = cnt

    for s_ in sorted(g[s]):
        if visited[s_] == 0:
            cnt += 1
            dfs(visited,s_,g)
    return

dfs(visited,r,g)
for i in visited[1:]:
    print(i)

# visited = [0, 1, 2, 3, 4, 0]
# visited[1:]
