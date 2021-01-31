# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        braces = {')':'(',
                  ']':'[',
                  '}':'{'}
        for symbol in s:
            if symbol in braces.values():
                stack.append(symbol)
            elif not stack or braces[symbol] != stack.pop():
                return False
        return not stack   
