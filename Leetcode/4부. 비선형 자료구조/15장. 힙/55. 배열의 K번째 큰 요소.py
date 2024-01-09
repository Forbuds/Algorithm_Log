오해하기 쉬운 힙의 특징: 힙은 정렬된 구조가 아니라는 점
최소 힙의 경우 - 부모 노드가 항상 작다는 조건만 만족, 서로 정렬되어있지 않다. (좌-우)
자식이 둘인 힙을 binary heap이라 하며, 널리 쓰임
힙 정렬의 부산물

힙의 용도
  우선순위 큐 - 활용: 다익스트라 알고리즘
  힙 정렬
  최소 신장 트리 - 프림 알고리즘
  중앙값의 근사값

https://leetcode.com/problems/kth-largest-element-in-an-array/description/

215. Kth Largest Element in an Array : Medium

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example 1:

  Input: nums = [3,2,1,5,6,4], k = 2
  Output: 5
Example 2:

  Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
  Output: 4

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]   # 숫자 -로 최대힙 만들어 주기
        heapq.heapify(nums)
        for _ in range(k):
            result = heapq.heappop(nums)
        return -result

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(len(nums)-k):    # n-k 시전
            result = heapq.heappop(nums)
        return heapq.heappop(nums)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k,nums)[-1]    # n smallest도 있다

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]      # 사실, sort를 이용한 내장 함수가 가장 빠르다(퀵..)
