import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().strip().split()))
q = [arr[0]]

for i in range(1,n):
    x = arr[i]
    if q[-1] < x:
        q.append(x)
    else:
        s = 0
        e = len(q)
        while s<e:
            mid = (s+e)//2
            if x <= q[mid]:
                e = mid
            else:
                s = mid+1
        q[s] = x
print(n-len(q))