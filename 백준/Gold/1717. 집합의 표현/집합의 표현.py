import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n, m = map(int, input().strip().split())
parent = [i for i in range(n+1)]

def find_parent(parent,x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parnet, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

for x in range(m):
    flag, a, b = map(int, input().strip().split())
    if flag==0: # 합집합
        union_parent(parent,a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print('yes')
        else:
            print('no')