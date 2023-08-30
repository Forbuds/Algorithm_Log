import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
m = int(input())

g = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m):
    u,v = map(int,input().split())
    g[u].append(v)
    g[v].append(u)

def dfs(visited,g,r):
    visited[r]=1
    for i in g[r]:
        if visited[i]==0:
            dfs(visited,g,i)
dfs(visited,g,1)
# print(g)
# print(visited)
print(visited.count(1)-1)
