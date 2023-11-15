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
        edges = sorted([tuple(map(int, input().split()))
                       for _ in range(n)], key=lambda x: x[2])
        result = 0
        for edge in edges:
            a, b, cost = edge
            if find(parent,a) == find(parent,b):
                result +=cost
                continue
            else:
                union(parent, a, b)
        print(result)