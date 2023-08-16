# Counter 활용
import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split()))
m = int(input())
targets = list(map(int, input().strip().split()))

arr = Counter(arr)
# print(arr)
print(' '.join(f'{arr[i]}' if i in arr else '0' for i in targets))