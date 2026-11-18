class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        old_sum = sum(arr[:k])
        if old_sum / k >= threshold:
            count = count + 1

        for i in range(k, len(arr)):
            old_sum = old_sum + arr[i] - arr[i-k]
            if old_sum / k >= threshold:
                count = count + 1
        return count
        