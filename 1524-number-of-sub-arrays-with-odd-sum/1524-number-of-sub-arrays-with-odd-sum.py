class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10**9 + 7

        even = 1
        odd = 0
        prefix = 0
        count = 0

        for i in range(len(arr)):
            prefix = prefix + arr[i]

            if prefix % 2 == 0:
                count = count + odd
                even = even + 1
            else:
                count = count + even
                odd = odd + 1

        return count % mod
        
        # count = 0

        # for i in range(len(arr)):
        #     for j in range(i, len(arr)):
        #         ans = sum(arr[i:j+1])

        #         if ans % 2 != 0:
        #             count += 1

        # return count % (10**9 + 7)