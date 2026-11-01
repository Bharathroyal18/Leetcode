class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_total=0
        for i in range(len(accounts)):
            total=0
            for j in range(len(accounts[i])):
                total=total+accounts[i][j]
            max_total=max(total,max_total)

        return max_total
        