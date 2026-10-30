class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2

            hours = 0
            for i in range(len(piles)):
                hours = hours + (piles[i] + mid - 1) // mid

            if hours <= h:     #6<8 [3,6,7,11]
                right = mid - 1
            else:
                left = mid + 1

        return left

        #left represents the minimum valid eating speed when the loop ends.