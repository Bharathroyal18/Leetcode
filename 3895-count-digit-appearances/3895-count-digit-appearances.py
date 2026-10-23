class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:

                                      #   Dry run
        numbers = map(str, nums)      # "12", "54", "32" , "22"   
        ans = "".join(numbers)        # "12543222"
        target = str(digit)           #  "2"
        return ans.count(target)      #   4