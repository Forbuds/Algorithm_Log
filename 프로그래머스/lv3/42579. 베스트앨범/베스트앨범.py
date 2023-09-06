from collections import OrderedDict,Counter
def solution(genres, plays):
    answer = []
    hash = {}
    hash_l = {}
    # plays = [500, 600, 500, 800, 2500]
    
    for i in range(len(plays)):
        x = genres[i]
        hash[x] = hash.get(x,[]) + [(plays[i],i)]
        hash_l[x] = hash_l.get(x,0) + int(plays[i])
    
    for x,c in sorted(hash_l.items(), key = lambda x:-x[1]):
        if len(hash[x]) < 2:
            answer.extend([hash[x][0][1]])
        else: 
            # print(sorted(hash[x], key = lambda x: (-x[0],x[1]))[:])
            answer.extend([b for a,b in  sorted(hash[x], key = lambda x: (-x[0],x[1]))[:2]])
    
    return answer