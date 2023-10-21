def solution(brown, yellow):
    
    for x in range(1,int(yellow**0.5)+1):
        
        if yellow%x==0: # 소인수이고
            if (brown-4)//2 == (x+yellow//x):
                break
                
    return [yellow//x+2,x+2]