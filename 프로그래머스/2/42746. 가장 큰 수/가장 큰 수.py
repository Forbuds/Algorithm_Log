from itertools import permutations

def solution(numbers):
    answer = ''.join(sorted([str(i) for i in numbers], key=lambda x: (-int((x*4)[:4]))))
    if int(answer)==0:
        return '0'
    else:
        return answer
    return 