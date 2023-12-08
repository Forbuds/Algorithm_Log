https://leetcode.com/problems/subsets/description/

78. Subsets
Medium

Given an integer array nums of unique elements, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

  Input: nums = [1,2,3]
  Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

  Input: nums = [0]
  Output: [[],[0]]

Constraints:

  1 <= nums.length <= 10
  -10 <= nums[i] <= 10
  All the numbers of nums are unique.


'''
  내 풀이
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(L,s):

            if len(s) == len(nums):
                result.append(s)
                return
            for i in range(L, len(nums)):
                s.append(nums[i])
                result.append(s[:])
                dfs(i+1,s)
                s.pop()


        result = []
        dfs(0,[])
        return result
'''
  해설지
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(L,s):

            result.append(s[:])

            for i in range(L, len(nums)):
                dfs(i+1,s+[nums[i]])

        result = []
        dfs(0,[])
        return result
