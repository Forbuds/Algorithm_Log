def solution(nums):
    answer = 0
    
    n = len(nums)//2
    
    hash = {}
    for x in nums:
        hash[x] = hash.get(x,0) + 1
    
    if n <= len(hash):
        answer = n
    else:
        answer = len(hash)
    
    return answer