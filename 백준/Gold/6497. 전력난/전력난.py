import sys
input = sys.stdin.readline
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

while 1:
    m,n = map(int, input().strip().split())
    # print('-',n,m)
    if n==0 and m==0:
        break
    else:
        parent = [i for i in range(m)]
        edges = []
        cnt = 0
        for i in range(n):
            a,b,cost = map(int, input().strip().split())
            edges.append((cost,a,b))
            cnt += cost
        edges = sorted(edges)
        result = 0
        for edge in edges:
            cost, a, b = edge
            if find(parent,a) != find(parent,b):
                union(parent,a,b)
            else:
                result +=cost
        print(result)