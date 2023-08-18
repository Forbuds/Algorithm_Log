import sys
input = sys.stdin.readline

n,k = map(int,input().strip().split())
# n^2도 괜찮음
k = k
arr = [i+1 for i in range(n)]
c = 0
print('<',end='')
while 1:
    if len(arr)==1:
        print(arr.pop(),end='>')
        break
    else:
        c = (c +k-1)%len(arr)
        # arr.pop(c)
        print(arr.pop(c),end=', ')