class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right + 1):
            n = i
            valid = True

            while n!=0:
                last = n % 10

                if last == 0 or i % last != 0:
                    valid = False
                    break

                n = n // 10

            if valid:
                ans.append(i)
        return ans