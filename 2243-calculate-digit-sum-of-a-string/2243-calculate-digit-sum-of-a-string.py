class Solution:
    def digitSum(self, s: str, k: int) -> str:

        while len(s) > k:
            ans = ""

            for i in range(0, len(s), k):
                group = s[i:i+k]

                total = 0
                for j in range(len(group)):
                    total = total + int(group[j])

                val = str(total)
                ans = ans + val

            s = ans

        return s
            