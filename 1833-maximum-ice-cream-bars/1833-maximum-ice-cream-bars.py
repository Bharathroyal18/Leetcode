class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        total=0
        count=0
        for i in range(len(costs)):
            total=total+costs[i]

            if total>coins:
                break

            count=count+1
            
        return count

        