class Solution:
    def areNumbersAscending(self, s: str) -> bool:

        ans = s.split()
        prev = 0

        for i in range(len(ans)):
            if ans[i].isdigit():
                num = int(ans[i])

                if num <= prev:
                    return False

                prev = num

        return True

        return False
        