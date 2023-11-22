hash = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
def solution(survey, choices):
    
    answer = ''

    for i in range(len(survey)):
        a,b = map(str,survey[i])
        c = choices[i]
        m,r = c//4,c%4
        if r==0:
            # print('점수 없음')
            continue
        elif m==0:
            # print(a, 4-r)
            hash[a] += 4-r
        else:
            # print(b,r)
            hash[b] += r
    # print(hash)
    
    answer += 'R' if hash['R'] >= hash['T'] else 'T'
    answer += 'C' if hash['C'] >= hash['F'] else 'F'
    answer += 'J' if hash['J'] >= hash['M'] else 'M'
    answer += 'A' if hash['A'] >= hash['N'] else 'N'
        
        
    return answer