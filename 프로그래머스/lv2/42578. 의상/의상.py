from itertools import combinations
def solution(clothes):
    answer = 1
    hash = {}
    # print(dir(combinations))
    for v,k in clothes:
        
        hash[k] = hash.get(k,[])+ [v]
        
    # len_tmp = {k:len(v) for k,v in hash.items()}
    # for i in range(len(hash)):
    #     for x in combinations(hash,i+1):
    #         tmp = 1
    #         for j in x:
    #             tmp*=len_tmp[j]  
    #         answer += tmp
    for k in hash.values():
        answer *= len(k)+1
    
    return answer - 1