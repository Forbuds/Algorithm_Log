def solution(numbers, hand):
    answer = ''
    right = 11
    left =  9

    # 나머지에 따라서 왼손일지, 오른손일지 구하는 방법
    # 이전 right의 나머지랑 
    # print([i//3 for i in range(1,13)])
    
    for n in numbers:
        if n==0:
            n = 11
        n = n-1
        r = n%3
        # print(n+1,r,f'left:{left+1}, right:{right+1}')
        if r==0:
            left = n
            answer += 'L'
        elif r==2:
            right = n
            answer += 'R'
        else:
            m = (n-1)//3
            cal = abs(left//3-m)+abs(left%3-r) - abs(right//3-m)-abs(right%3-r)
            # print(abs(left//3-m)+abs(left%3-r),abs(right//3-m)+abs(right%3-r),m+r,cal)
            if cal < 0:
                left = n
                answer += 'L'
            elif cal > 0:
                right = n
                answer += 'R'
            else:
                # print('same', hand)
                if hand == 'left':
                    left = n
                    answer += 'L'
                else:
                    right = n
                    answer += 'R'
                
        
    return answer