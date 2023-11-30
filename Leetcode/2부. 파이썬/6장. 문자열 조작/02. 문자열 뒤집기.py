https://leetcode.com/problems/reverse-string/submissions/

Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 
Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        다른 풀이인데 비슷할지도
        """
        """
        풀이 1. 투포인터, 181ms
        """
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


        """
        풀이 2. 파이썬 기능, 190ms
        """

        s.reverse()

        """
        풀이 3. 파이썬 기능
        """

        s[:] = s[::-1]   # 원래는 s = s[::-1]도 가능
