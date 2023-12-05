https://leetcode.com/problems/3sum/description/
  
15. 3Sum : Medium

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:

  Input: nums = [-1,0,1,2,-1,-4]
  Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
  nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
  nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
  nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
  The distinct triplets are [-1,0,1] and [-1,-1,2].
  Notice that the order of the output and the order of the triplets does not matter.
Example 2:

  Input: nums = [0,1,1]
  Output: []
  Explanation: The only possible triplet does not sum up to 0.
Example 3:

  Input: nums = [0,0,0]
  Output: [[0,0,0]]
  Explanation: The only possible triplet sums up to 0.
 

Constraints:

  3 <= nums.length <= 3000
  -105 <= nums[i] <= 105

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
            O(N*3)
            Time Limit Exceeded
            308 / 312 testcases passed
        '''
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i] + nums[j] + nums[k] ==0:
                        tmp = [nums[i] , nums[j] , nums[k]]
                        if tmp not in result:
                            result.append([nums[i] , nums[j] , nums[k]])
        return result

        # 여기에, 중복된 값 건너 뛰는 방법은 (브루트 포스는 중복값이 발생할 가능성 높다, 처리해줘야 함)
        if nums[i] == nums[i-1]:
            continue
        # 그래도 타임아웃이 걸린다.

        '''
            투포인터
            i,   left -> <- right로 sum 계산
        '''
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n):
            if i>0 and nums[i-1] == nums[i]:
                continue
            left, right = i+1, n-1
            while left<right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum >0:
                    right -=1
                else:
                    result.append([nums[i] , nums[left] , nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left +=1
                    while left < right and nums[right-1] == nums[right]:
                        right -=1
                    left += 1 
                    right -=1
        return result
