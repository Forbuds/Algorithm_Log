import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
arr = sorted(arr)
s = []
def dfs(c,l):
    if l==m:
        print(' '.join(map(str,s)))
        return
    else:
        tmp = 0
        for i in range(n):
            if tmp != arr[i]:
                s.append(arr[i])
                dfs(i,l+1)
                tmp = s.pop()
dfs(0,0)