def solution(numbers):
    from itertools import permutations
    answer = 0
    arr = []
    for i in range(len(numbers)):
    
        for x in permutations(numbers,i+1):
            # print(int(''.join(x)))
            arr.append(int(''.join(x)))
    arr = list(set(arr))
    print(arr)
    
    for n in arr:
        if n<2:
            continue
        check = True            
        for i in range(2,int(n**0.5) + 1):        
            if n % i == 0:                        
                check = False
                break
        if check:
            answer+=1                   


    return answer