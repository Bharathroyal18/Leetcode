class Solution:
    def beautySum(self, s: str) -> int:

        total = 0
        for i in range(len(s)):
            d = {}
            for j in range(i, len(s)):
                if s[j] in d:
                    d[s[j]] = d[s[j]] + 1
                else:
                    d[s[j]] = 1

                beauty = max(d.values()) - min(d.values())
                total = total + beauty
        return total


        # total = 0
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         ans = s[i:j+1]

        #         d = {}
        #         for k in range(len(ans)):
        #             if ans[k] in d:
        #                 d[ans[k]] = d[ans[k]] + 1
        #             else:
        #                 d[ans[k]] = 1

        #         beauty = max(d.values()) - min(d.values())
        #         total = total + beauty

        # return total