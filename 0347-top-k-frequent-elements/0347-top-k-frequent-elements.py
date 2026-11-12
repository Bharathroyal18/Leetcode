class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        ans = sorted(d, key=d.get, reverse=True)

        return ans[:k]

        # arr = list(d.items())                                #dict to list
        # arr.sort(key=lambda x: x[1], reverse=True)      #x[0]:key, x[1]:frequency

        # result = []
        # for i in range(k):
        #     result.append(arr[i][0])
        # return (result)
        