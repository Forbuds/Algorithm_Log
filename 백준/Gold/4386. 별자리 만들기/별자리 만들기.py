import sys
from itertools import combinations as combi
input = sys.stdin.readline
def find(parent, x):                            # 유니온 파인드
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]
def union(parent,x,y):
    x = find(parent,x)
    y = find(parent,y)
    if x<y:
        parent[y] = x
    else:
        parent[x] = y
n = int(input())
points = {i: tuple(map(float,input().strip().split())) for i in range(n)}
# print(points)
edges = []
parent = [i for i in range(n)]
result = 0
for x in range(n-1):
    for y in range(x+1,n):
        # print(x,y)
        cost = ((points[x][0]-points[y][0])**2 + (points[x][1]-points[y][1])**2)**0.5
        edges.append((cost,x,y))
edges = sorted(edges)
for edge in edges:
    cost, x, y = edge
    if find(parent,x) != find(parent, y):
        union(parent,x,y)
        result += cost
print(format(result,'.2f'))