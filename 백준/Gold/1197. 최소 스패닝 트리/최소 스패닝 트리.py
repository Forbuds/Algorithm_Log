import sys
input = sys.stdin.readline

def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]

def union(parent, a,b):
    a = find(parent, a)
    b = find(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

v,e = map(int, input().strip().split())
parent = [i for i in range(v+1)]
edges = []
result = 0
for _ in range(e):
    a,b, cost = map(int, input().strip().split())
    edges.append((cost,a,b))

edges = sorted(edges)
for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent,b):
        union(parent,a,b)
        result += cost
print(result)