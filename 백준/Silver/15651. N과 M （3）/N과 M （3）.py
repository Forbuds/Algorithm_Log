import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().strip().split())
arr = []
s = deque([])
def dfs(l):
    if l==m:
        print(*s,sep=' ')
        return
    else:
        for i in range(n):
            s.append(i+1)
            dfs(l+1)
            s.pop()

dfs(0)