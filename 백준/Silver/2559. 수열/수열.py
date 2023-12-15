import sys
input = sys.stdin.readline
n,k = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
# print(arr[0], arr[k-1])
if k==1:
    print(max(arr))
else:
    s, e = 0, k-1
    tmp = sum(arr[0:k])
    result = tmp
    # print(result)
    while s<e and e<n-1:
    
        e += 1
        tmp = tmp + arr[e] - arr[s]
        s += 1
        # print(tmp,  arr[e])
        result = max(result, tmp)
    
    print(result)