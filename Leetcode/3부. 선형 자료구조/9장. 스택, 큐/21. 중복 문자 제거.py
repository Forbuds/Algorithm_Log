https://leetcode.com/problems/remove-duplicate-letters/submissions/

316. Remove Duplicate Letters : Medium

Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
the smallest in lexicographical order among all possible results.

Example 1:

  Input: s = "bcabc"
  Output: "abc"
Example 2:

  Input: s = "cbacdcbc"
  Output: "acdb"
 
Constraints:

  1 <= s.length <= 104
  s consists of lowercase English letters.
 
Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        '''
          실패
        '''
        # counter, stack = collections.Counter(s), []
        # for x in s:
        #     print(f'current: {stack}, {x}, {counter[x]}')
        #     if x not in stack:
        #         stack.append(x)
        #         counter[x] -= 1
        #     else: # 이미 있는 경우
        #         if counter[x]==0:
        #             continue
        #         else:
        #             print(x,x<stack[-1])
        #             if x < stack[-1] :
        #                 counter[x] = 0
        #             else:
        #                 stack.remove(x)
        #                 stack.append(x)
        #                 counter[x] -= 1
        # return stack

        '''
          재귀를 이용한 풀이
        '''

        '''
        스텍을 이용한 문자 제거
        '''
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
          counter[char] -= 1

          if char in seen:   # 있다면 pass
            continue

          while stack and char < stack[-1] and counter[stack[-1]]>0:
            # stack[-1]이 유일한 친구라면 -> counter[stack[-1]]==0: 멈춤 
            # stack이 없다면: 멈춤
            # char이 뒤에 있다면: 멈춤  a < b 라면 고대로 넣어준다.
            seen.remove(stack.pop())       # 위 조건들이 아니라면 뽑아낸다.

          '''
          while문에 대한 설명

          if
          # 앞에꺼가 유일한 친구면 못뺀다. stack에 차근차근 쌓아주고, cbacdcbc에서의 d 같이
          # stack이 비어있다면 넣어주고
          # char이 뒤쳐지면 넣어준다.

          else
          # 앞에꺼가 유일하지 않거나 char이 앞서거나(순서: char stack[-1]) 그러면 stack.pop() 그걸 또 seen.remove()
          '''
            
          stack.append(char)
          seen.add(char)

        return ''.join(stack)
