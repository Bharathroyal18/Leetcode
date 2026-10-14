
class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if not s[i].isdigit():
                stack.append(s[i])
            elif stack:
                stack.pop()

        return "".join(stack)
