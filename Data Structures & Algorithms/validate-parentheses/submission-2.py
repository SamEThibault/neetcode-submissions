class Solution:
    def isValid(self, s: str) -> bool:
        matching = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            if char == ')' or char == '}' or char == ']':
                if len(stack) == 0:
                    return False
                if stack.pop() != matching[char]:
                    return False

        return len(stack) == 0
