import sys
input = sys.stdin.readline

n = int(input())
arr = [tuple(map(int, input().strip().split())) for _  in range(n)]
# print(n,arr)
# print(sorted(arr,key=lambda x:(x[0],x[1])))
for i in sorted(arr,key=lambda x:(x[0],x[1])):
    print(i[0],i[1])