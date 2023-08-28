import sys
input = sys.stdin.readline

n,m = map(int, input().strip().split())

g = list(map(int, input().strip().split()))
# print(n,m,g)
g = sorted(list(set(g)))
# print(g,'dddddd')
s = []
def dfs(c):
    if len(s)==m:
        print(' '.join(map(str,s)))
    else :
        for i in range(c,len(g)):
            s.append(g[i])
            dfs(i)
            s.pop()

dfs(0)