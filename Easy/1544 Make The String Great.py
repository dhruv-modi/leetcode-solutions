# https://leetcode.com/problems/make-the-string-great/
    
# Given a string s of lower and upper case English letters.

# A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

# 0 <= i <= s.length - 2
# s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
# To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

# Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

# Notice that an empty string is also good.

# Constraints:

# 1 <= s.length <= 100
# s contains only lower and upper case English letters.

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for character in s:
            if stack:
                if stack[-1] != character and (stack[-1].upper() == character or stack[-1] == character.upper()):
                    stack.pop()
                else:
                    stack.append(character)
            else:
                stack.append(character)
        return ''.join(stack)
        
                    
