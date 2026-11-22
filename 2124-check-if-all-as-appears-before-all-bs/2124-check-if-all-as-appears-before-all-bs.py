class Solution:
    def checkString(self, s: str) -> bool:

        for i in range(len(s)):
            if s[i] == 'a':
                if 'b' in s[:i]:
                    return False

        return True