import sys
input = sys.stdin.readline
n,m = map(int, input().strip().split())
arr = list(map(int,input().strip().split()))
a,b = 0,1
cnt = 0
while a<=b and b<=n:
    total = sum(arr[a:b])
    if total ==m:
        b +=1
        cnt +=1
    elif total <m :
        b +=1
    else:
        a +=1
print(cnt)