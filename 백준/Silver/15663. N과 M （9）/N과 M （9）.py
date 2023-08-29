import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())
arr = sorted(list(map(int, input().strip().split())))
s = []
v = [0]*(n)
def per(l,index):
    tmp = 0
    if l==m:
        print(' '.join(map(str,s)))
        return
    else:
        for i in range(n):
            if v[i]==0 and tmp!=arr[i]:
                tmp = arr[i]
                v[i] = 1
                s.append(arr[i])
                per(l+1,i)
                v[i] = 0
                s.pop()

per(0,0)