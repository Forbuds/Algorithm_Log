238. Product of Array Except Self : Medium

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
---> You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

  Input: nums = [1,2,3,4]
  Output: [24,12,8,6]
Example 2:

  Input: nums = [-1,1,0,-3,3]
  Output: [0,0,9,0,0]
 
Constraints:

  2 <= nums.length <= 105
  -30 <= nums[i] <= 30
  The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
                                                                                                                    
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      '''
          양쪽에서 누적 곱
      '''
      p = 1
      out = []

      for i in range(len(nums)):
        out.append(p)
        p = p*nums[i]
        # a = [1, 1, 2, 6]

      p = 1
      for i in range(len(nums)-1,-1,-1):
        out[i] = out[i]*p
        p = p*nums[i]
        # b = [24, 12, 4, 1]

      # a.*b = [24, 12, 8, 6]
      return out

      '''
          이 코드가 좀 더 빠름 10ms 정도
      '''
      p = 1
      out = [0]*len(nums)
      for i in range(len(nums)):
        out[i] = p
        p *= nums[i]
      p = 1
      for i in range(len(nums)-1,-1,-1):
        out[i] *= p
        p *= nums[i]
      return out
