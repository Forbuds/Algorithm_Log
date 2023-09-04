from collections import deque
def solution(numbers, target):
    answer = 0
    
    def dfs(l,result):
        nonlocal answer
        
        if l==len(numbers):
            if result == target:
                answer+=1
            return
        
        else:
            dfs(l+1,result+numbers[l])
            dfs(l+1,result-numbers[l])
        
    dfs(0,0)
    
    
    return answer