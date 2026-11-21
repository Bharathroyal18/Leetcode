class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:

        result=[]
        
        for i in range(len(candies)):
            ans=candies[i]+extraCandies

            if ans>=max(candies):
                result.append(True)
            else:
                result.append(False)

        return result
        