https://leetcode.com/problems/most-common-word/description/

819. Most Common Word
Easy
1.6K
3K
Companies
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

Example 1:

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
  "hit" occurs 3 times, but it is a banned word.
  "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
  Note that words in the paragraph are not case sensitive,
  that punctuation is ignored (even if adjacent to words, such as "ball,"), 
  and that "hit" isn't the answer even though it occurs more because it is banned.
Example 2:
  Input: paragraph = "a.", banned = []
  Output: "a"
 

Constraints:

  1 <= paragraph.length <= 1000
  paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
  0 <= banned.length <= 100
  1 <= banned[i].length <= 10
  banned[i] consists of only lowercase English letters.
  Accepted
  338.9K
  Submissions
  762.5K
  Acceptance Rate
  44.4%

class Solution:
    from collections import Counter
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

       words = [word for word in re.sub('[^\w]',' ', paragraph).lower().split() if word not in banned]

       # re.sub('[^\w]',' ', paragraph) : 문자가 아닌 것들은 모두 공백으로 치환
       
       count = Counter(words)
       print(count.most_common(1))      # [('ball', 2)]
       print(count.most_common(2))      # [('ball', 2), ('bob', 1)]

       return count.most_common(1)[0][0]
