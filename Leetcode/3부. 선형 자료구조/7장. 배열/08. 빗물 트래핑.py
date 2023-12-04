https://leetcode.com/problems/trapping-rain-water/description/

42. Trapping Rain Water : Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

  Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
  Output: 6
  Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

  Input: height = [4,2,0,3,2,5]
  Output: 9

Constraints:

  n == height.length
  1 <= n <= 2 * 104
  0 <= height[i] <= 105

class Solution:
    def trap(self, height: List[int]) -> int:

        '''
            2*10^4   * 10^5 정도 됨. 최악의 풀이
            한 층마다, 물 채워 나가는 형식
            Time Limit Exceeded 318/322 testcases passed
        '''
        result = 0
        m = max(height)+1
        for h in range(1,m):
            tmp = ''.join(map(str,[ 1 if i >= h else 0 for i in height ])).strip('0')
            result += tmp.count('0')
        return result

        '''
            투 포인터를 최대로 이동
            낮은 쪽은 항상 채워지는 원리
        '''
        if not height:
            return 0
        result = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]

        while left<right:                           # 투포인터라서 항상 유의
            # print(left_max, height[left], right_max, height[right])
            left_max , right_max = max(left_max, height[left]), max(right_max, height[right])
                                                    # 현재가 높다면, 현재로 max를 먼저 바꿔준다.

            if left_max <= right_max:               # 등호 붙던 말던 상관 없음, 큰 높이가 버티고 서있는다 = 작은 높이가 움직임
                result += left_max - height[left]   # 현재가 높다면 0, 원래가 높았다면 차이만큼
                left +=1                            # 볼륨 채운 다음에 움직임
                # height[left] = left_max : 확인용
            else:
                result += right_max - height[right]
                right -=1
                # height[right] = right_max : 확인용
            # print(left, right, height)
        return result
