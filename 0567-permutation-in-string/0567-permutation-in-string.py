class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        d = {}
        for i in range(len(s1)):
            if s1[i] in d:
                d[s1[i]] = d[s1[i]] + 1
            else:
                d[s1[i]] = 1

        k = len(s1)  

        d2 = {}
        for i in range(k):
            if s2[i] in d2:
                d2[s2[i]] = d2[s2[i]] + 1
            else:
                d2[s2[i]] = 1

        if d == d2:
            return True

        for i in range(k, len(s2)):          #i=2   i-k = 2-2 = 0
            d2[s2[i-k]] = d2[s2[i-k]] - 1

            if d2[s2[i-k]] == 0:
                del d2[s2[i-k]]

            if s2[i] in d2:
                d2[s2[i]] = d2[s2[i]] + 1
            else:
                d2[s2[i]] = 1

            if d == d2:
                return True

        return False