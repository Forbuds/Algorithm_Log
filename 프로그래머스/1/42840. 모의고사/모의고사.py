def solution(answers):
    answer = []
    a,b,c = 0,0,0
    l = len(answers)
    l_c = [3,1,2,4,5]
    l_b = [1,3,4,5]
    
    # 3311224455
    # 0123456789
    # 0011223344
    # 012345678910
    # 2123
    # 0011223344556677
    
    for i in range(l):
        # print(1+(i%5))
        ans = answers[i]
        # print(ans, (i+1)%6)
        if 1+(i%5)==ans:
            a+=1
        if i%2==0 and ans==2:
            b+=1
        if i%2==1 and ans==l_b[(i//2)%4]:
            b+=1
        # 홀수면 1,3,4,5
        # 짝수면 2
        if l_c[(i//2)%5] == ans:
            c+=1
    print(a,b,c)
    tmp = [(a,1),(b,2),(c,3)]
    tmp = sorted(tmp, key = lambda x: (-x[0]))
    flag = -1
    print(tmp)
    for x,idx in tmp:
        if not answer:
            answer.append(idx)
            flag = x
        else:
            if flag ==x:
                answer.append(idx)
    return sorted(answer)
