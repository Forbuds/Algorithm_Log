class Solution:
    import re
    from collections import deque
    def isPalindrome(self, s: str) -> bool:
        '''
            풀이 1. 데크 자료형
        '''
        strs = deque([])
        for x in s:
            if x.isalnum():
                strs.append(x.lower())
        while len(strs)>1:
            if strs.popleft() != strs.pop():
                return False
        return True  # 데크 자료형은 슬라이싱 불가 
        
        '''
            풀이 2. 하나씩 확인, 리스트 슬라이싱
        '''
        
        s = [x.lower() for x in s if x.isalnum()]
        return s == s[::-1]


        '''
            BEST! 풀이 3. RE, 리스트 슬라이싱
        '''

        s = s.lower()
        s = re.sub('[^a-z0-9]','',s)    # sub : 치환한다.
                                        #  ^ : 피해야 할 문자들   
                                        # []이걸 치환한다. [^]이거말고 다른걸 치환한다.
