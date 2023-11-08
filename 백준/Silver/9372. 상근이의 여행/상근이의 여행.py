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

t = int(input())
for _ in range(t):
    v,e = map(int, input().strip().split())
    parent = [i for i in range(v+1)]
    cnt = 0
    for _ in range(e):
        a,b = map(int, input().strip().split())
        if find(parent, a) != find(parent,b):
            union(parent,a,b)
            cnt += 1
    print(cnt)