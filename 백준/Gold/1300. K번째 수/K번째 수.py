# method 숫자
# target count
# display 숫자
#
# method index +-
# target 숫자
# display 숫자
import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
s,e = 0, n**2

while s<=e:
    count = 0
    mid = (s+e)//2
    for i in range(1,n+1):
        count += min(mid//i ,n)
    if count < k:
        s = mid +1
    else:
        e = mid -1
print(s)