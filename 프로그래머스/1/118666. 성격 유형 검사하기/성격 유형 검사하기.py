hash = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
def solution(survey, choices):
    
    answer = ''

    for i in range(len(survey)):
        if choices[i] - 4 < 0: 
            hash[survey[i][0]] += 4 - choices[i]

        elif choices[i] - 4 > 0: 
            hash[survey[i][1]] += choices[i] - 4
    # print(hash)
    
    answer += 'R' if hash['R'] >= hash['T'] else 'T'
    answer += 'C' if hash['C'] >= hash['F'] else 'F'
    answer += 'J' if hash['J'] >= hash['M'] else 'M'
    answer += 'A' if hash['A'] >= hash['N'] else 'N'
        
    return answer
