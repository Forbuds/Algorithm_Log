import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())
v = [0]*n
def dfs(l):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    else:
        for i in range(n):
            s.append(i+1)
            dfs(l+1)
            s.pop()
s = []
dfs(0)