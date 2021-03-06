# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/submissions/
    
# Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

# We repeatedly make duplicate removals on S until we no longer can.

# Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

# Note:

# 1 <= S.length <= 20000
# S consists only of English lowercase letters.

class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for char in S:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
            
        
