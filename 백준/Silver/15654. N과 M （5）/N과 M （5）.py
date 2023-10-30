import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())
arr = list(map(int,input().strip().split()))
arr = sorted(arr)
v = [0]*n
s = []
def dfs(c,l):
    if l==m:
        print(' '.join(map(str,s)))
        return
    else:
        for i in range(0,n):
            if v[i]==0:
                s.append(arr[i])
                v[i]=1
                # print(f'-------{s}')
                dfs(c,l+1)
                s.pop()
                v[i]=0

dfs(0,0)