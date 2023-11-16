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
        
        
n, m = map(int, input().strip().split())
parent = [i for i in range(n+1)]                            # 부모 초기화(자기자신)
points = {}                                                 # 정점 위치 별 좌표를 딕셔너리로 만들어 둔다.
for i in range(n):
    points[i+1]=tuple(map(int, input().strip().split()))
# print(points)

edges = []                                                  # 거리 정보가 주어지지 않았으므로 직접 구해야 한다. nC2로
for x in combi([i+1 for i in range(n)],2):
    a,b = x
    s = pow(pow(points[a][0]-points[b][0],2)+pow(points[a][1]-points[b][1],2),0.5)
    edges.append(( s, a,b))
edges = sorted(edges)                            # 정렬 - 크루스칼 쓰기 위해

for i in range(m):
    x,y = map(int, input().strip().split())
    union(parent, x,y)
result = 0
# print(parent)
for edge in edges:
    cost,x,y = edge
    if find(parent,x) != find(parent,y):
        union(parent,x,y)
        result += cost

print(format(result, ".2f"))