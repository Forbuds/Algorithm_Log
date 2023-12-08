https://leetcode.com/problems/permutations/submissions/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(l,s):
            if len(s) == len(nums):
                result.append(list(s))
                return

            for i in range(len(nums)):
                if nums[i] in s:
                  continue
                else:
                  s.append(nums[i])
                  dfs(i+1, s )
                  s.pop()
        result = []
        dfs(0,[])
        return result
