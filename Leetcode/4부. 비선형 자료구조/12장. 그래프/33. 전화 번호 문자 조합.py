https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(l,s):
            if len(s)==len(digits):
                result.append(s)
                return
            
            for i in range(l, len(digits)):
                for j in num[digits[i]]:
                      dfs(i+1,s+j)
        if digits =='':
          return []
        num = {'2':'abc','3':'def','4':'ghi',
            '5':'jkl','6':'mno','7':'pqrs',
            '8':'tuv','9':'wxyz'}
        result = []
        dfs(0,'')

        return result
