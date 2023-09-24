class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for char in s:
            if char == '*':
                while stack and stack[-1] == '*':
                    stack.pop()
                if stack:
                    stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)