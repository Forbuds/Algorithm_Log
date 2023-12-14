def solution(gems):
    n = len(set(gems))
    answer = [0,len(gems)-1]
    left, right = 0, 0
    dic = {gems[0]:1}
    stop = False
    while left <= right and right<len(gems):
        if len(dic)< n:
            right += 1
            if right == len(gems):
                break
            dic[gems[right]] = dic.get(gems[right], 0) + 1
            # print(n,right, dic)

        else:
            if right-left < answer[1] - answer[0]:
                answer = [left, right]
            else:
                dic[gems[left]] -= 1
                if dic[gems[left]] == 0:
                    del dic[gems[left]]
                left += 1
    
    return [answer[0]+1, answer[1]+1]