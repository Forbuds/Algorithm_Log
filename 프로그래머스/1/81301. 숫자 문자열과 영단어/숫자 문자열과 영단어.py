hash = {'zero':'0',
'one':'1',
'two':	'2',
'three':	'3',
'four':	'4',
'five':	'5',
'six':	'6',
'seven':	'7',
'eight':	'8',
'nine':	'9'}
# print(hash)
def solution(s):
    answer = ''
    tmp=''
    for x in s:
        if x in hash.values():
            answer += x
        else:
            tmp += x
            if tmp in hash.keys():
                answer += hash[tmp]
                tmp = ''
        # print(x)
    return int(answer)