https://leetcode.com/problems/longest-palindromic-substring/description/

5. Longest Palindromic Substring  : Medium

Given a string s, return the longest palindromic substring in s.

Example 1:

  Input: s = "babad"
  Output: "bab"
  Explanation: "aba" is also a valid answer.
Example 2:

  Input: s = "cbbd"
  Output: "bb"
 

Constraints:

  1 <= s.length <= 1000
  s consist of only digits and English letters.
  
class Solution:
    def longestPalindrome(self, s: str) -> str:

        '''
            최악의 풀이법 : DP로 풀기
        '''
        n = len(s)
        dp = [ (1,w) for w in s+' ']
        for i in range(1,n+1):
            for j in range(i):
                tmp = s[j:i]
                if tmp == tmp[::-1]:
                    dp[i]  = max(dp[i], (len(tmp), tmp ))
        return max(dp)[1]

        '''
            중심에서 확장하는 슬라이딩 윈도우
        '''
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[right] == s[left] : # 계속 확장하니까, 같은지 확인하고 길게 가는 방법
                left -=1
                right +=1
            return s[left+1 : right ]                                    # left +1 인 것에 주목: 0부터 시작하는 방법 left+1 ~ right-1

        # 먼저, 예외처리
        if len(s)<2 or s==s[::-1]:
            return s
        else:
            result = ''
            for i in range(len(s) - 1):
                print(f'----{i}')
                result = max(result, expand(i,i+1), expand(i, i+2), key = len)
                # i+1은 짝수 파트 : (3)4 (4-)4 -> (2,3,4)5  (3,4)5     -> 0,2,4,6, ...
                # i+2는 홀수 파트 : (3,4)5 (4)5 -> (2,3,4,5)6  (3,4,5)6      -> 1,3,5, ...
            return result
