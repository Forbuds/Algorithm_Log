from itertools import combinations as combi
def det(x):
    
    for i in range(2,int(x**(0.5))+1):
        if x%i==0:
            return 0
    return 1
    
def solution(nums):
    answer = 0
    for arr in combi(nums,3):
        x = sum(arr)
        answer += det(x)
    

    return answer