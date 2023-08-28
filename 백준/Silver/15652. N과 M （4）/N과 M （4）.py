import sys
import itertools
input = sys.stdin.readline

n, m = map(int, input().strip().split())

for i in itertools.combinations_with_replacement([x+1 for x in range(n)],m):
    print(' '.join(map(str,i)))