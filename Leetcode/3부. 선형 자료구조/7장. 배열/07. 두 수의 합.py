https://leetcode.com/problems/two-sum/description/

1. Two Sum : Easy

Companies
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

  Input: nums = [2,7,11,15], target = 9
  Output: [0,1]
  Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

  Input: nums = [3,2,4], target = 6
  Output: [1,2]
Example 3:

  Input: nums = [3,3], target = 6
  Output: [0,1]
 

Constraints:

  2 <= nums.length <= 104
  -109 <= nums[i] <= 109
  -109 <= target <= 109
  Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
            조합
        '''
        for num in itertools.combinations([i for i in range(len(nums))],2):
            a, b = num
            if nums[a]+nums[b] == target:
                return list(num)

        '''
            for i - i+1 ~전체 : 이중포문
        '''

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
        
        '''
           타겟에서 빼서, 전체에서 in으로 찾음 - in이 더 빠르다. 
        '''

        for i,n in enumerate(nums):
            sub = target - n
            if sub in nums[i+1:]:
                return i, nums[i+1:].index(sub) + i +1

        '''
            딕셔너리 - key, value 바꿔서
        '''
        
        hash = {}
        for i,num in enumerate(nums):
            
            if target - num in hash and hash[target-num] != i:
                return hash[target-num], i
            hash[num] = i
