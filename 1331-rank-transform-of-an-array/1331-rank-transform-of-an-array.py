class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        sorted_arr = sorted(set(arr))
        rank = {}           #[10,20,30,40]

        for i in range(len(sorted_arr)):
            rank[sorted_arr[i]] = i + 1       #{10:1,20:2,30:3,40:4}

        ans = []
        for i in range(len(arr)):
            ans.append(rank[arr[i]])           #[4,1,2,3]

        return ans