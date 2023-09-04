def solution(participant, completion):
    answer = ''
    
    hash = {}
    
    for x in participant:
        hash[x] = hash.get(x,0) +1
    for x in completion:
        hash[x] -=1
    
    # print(hash.items())
    tmp = {v:k for k,v in hash.items() }
    # print(tmp[1])
    
    return tmp[1]