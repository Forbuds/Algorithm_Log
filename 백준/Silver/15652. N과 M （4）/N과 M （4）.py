import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
s = []

def com(l, index):
    if l == m:
        print(' '.join(map(str,s)))
        return
    else:
        for i in range(index,n):
            s.append(i+1)
            com(l+1,i)
            s.pop()

com(0,0)