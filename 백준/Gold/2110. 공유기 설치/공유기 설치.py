import sys
input = sys.stdin.readline

n, c = map(int, input().strip().split())
arr = [ int(input()) for _ in range(n)]
arr = sorted(arr)
d = 0

s = 1
e = arr[-1]-arr[0]   #거리로 산정
cnt = 0
while s<=e:
    mid = (s+e)//2
    n_c = arr[0]
    cnt = 1

    for i in range(n):
        if arr[i]-n_c >= mid:
            cnt+=1
            n_c = arr[i]
    # print(s,mid,e,cnt,c)
    if cnt >= c:    # 거리가 너무 가깝다
        s = mid + 1
    else:
        e = mid - 1
print(e)