https://leetcode.com/problems/valid-parentheses/description/

20. Valid Parentheses : Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.
An input string is valid if:
  Open brackets must be closed by the same type of brackets.
  Open brackets must be closed in the correct order.
  Every close bracket has a corresponding open bracket of the same type.
 
Example 1:

  Input: s = "()"
  Output: true
Example 2:

  Input: s = "()[]{}"
  Output: true
Example 3:

  Input: s = "(]"
  Output: false
 

Constraints:

  1 <= s.length <= 104
  s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        table = {')': '(', ']': '[','}': '{'}
        stack = []
        for x in s:
            if x not in table:  #'('
                stack.append(x)
            elif not stack or table[x] != stack.pop():  # ')'의 hash값인 '('와 stack의 '('가 일치해야 함 -> 그렇지 않으면 false 
            #그리고, stack이 비어있는데 ) 부터 나오면 안됨
                return False
        return len(stack) == 0
