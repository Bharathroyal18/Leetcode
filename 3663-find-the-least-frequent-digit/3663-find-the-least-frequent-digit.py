class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        d = {}

        while n != 0:
            val = n % 10

            if val in d:
                d[val] = d[val] + 1
            else:
                d[val] = 1

            n = n // 10

        least = min(d.values())
        ans = []
        for key in d:
            if d[key] == least:
                ans.append(key)

        return min(ans)
        