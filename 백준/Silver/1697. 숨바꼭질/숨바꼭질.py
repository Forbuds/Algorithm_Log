import sys
input = sys.stdin.readline
from collections import deque
n, k = map(int, input().strip().split())
q = deque([n])
arr = [0]*(100001)
def bfs():
    while q:
        n_c = q.popleft()
        if n_c ==k:
            return arr[n_c]
        for x in (n_c-1,n_c+1,2*n_c):
            if 0<=x<=100000 and arr[x]==0:
                arr[x] = arr[n_c] +1
                q.append(x)
print(bfs())