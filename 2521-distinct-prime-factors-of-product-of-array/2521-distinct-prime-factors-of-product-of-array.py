class Solution:
    def distinctPrimeFactors(self, nums: list[int]) -> int:
        n = 1
        for i in nums:
            n = n*i            #product[10080]

        i = 2
        factors = []
        while n>=i:
            if n % i == 0:
                factors.append(i)
                n = n // i          #prime factors [2, 2, 2, 2, 2, 3, 3, 5, 7]
            else:
                i += 1

        d = {}
        for i in range(len(factors)):
            if factors[i] in d:
                d[factors[i]] = d[factors[i]] + 1
            else:                                         #{2:5,3:2,5:1,7:1} length=4
                d[factors[i]] = 1

        return len(d)
        