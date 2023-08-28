import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())
s = []
def per(L, index):
    if L==m:
        print(' '.join(map(str,s)))
        return
    else:
        for i in range(index,n):
            s.append(i+1)
            per(L+1,i+1)
            s.pop()
per(0,0)