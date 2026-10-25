class Solution:
    def distinctPrimeFactors(self, nums: list[int]) -> int:
        n = 1
        for i in nums:
            n = n*i

        i = 2
        factors = []
        while n>=i:
            if n % i == 0:
                factors.append(i)
                n = n // i
            else:
                i += 1

        d = {}
        for i in range(len(factors)):
            if factors[i] in d:
                d[factors[i]] = d[factors[i]] + 1
            else:
                d[factors[i]] = 1

        return len(d)
        