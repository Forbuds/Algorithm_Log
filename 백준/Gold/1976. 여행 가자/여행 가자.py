import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
g = []
for i in range(n):
    g.append(list(map(int,input().strip().split())))

arr = list(map(int,input().strip().split()))
parent = [i for i in range(n)]
tmp = -1
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
for x in range(n):
    for y in range(x,n):
        # print(x,y)
        if g[x][y]==1:
            union(parent,x,y)
# print(parent)
flag = True
for x in arr:
    if tmp!=-1:
        if find(parent,tmp) != find(parent, x-1):

            print('NO')
            flag = False
            break
        # if find(parent,tmp) != find(parent[x]):
    else:
        pass
    tmp = x-1
if flag:
    print('YES')