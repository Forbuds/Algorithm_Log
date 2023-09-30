'''
https://www.codetree.ai/missions/2/problems/conveyor-belt/description
'''

import sys
sys.stdin = open("E:\노트북\취준\삼성\sample_input.txt",'r')

Case = int(input())

def shift(arr,n):
    tmp = arr[0][-1]
    for i in range(n-1,0,-1):
        arr[0][i] = arr[0][i-1]
    arr[0][0] = arr[1][0]
    for i in range(0,n-1):
        arr[1][i] = arr[1][i+1]
    arr[1][-1] = tmp
    return arr


for c in range(Case):
    n,t = map(int,input().strip().split())
    arr = []
    arr.append(list(map(int,input().strip().split())))
    arr.append(list(map(int, input().strip().split()))[::-1])
    for i in range(t):
        arr = shift(arr,n)
    print(' '.join(map(str,arr[0])))
    print(' '.join(map(str, arr[1]))[::-1])
    print('-'*30)
