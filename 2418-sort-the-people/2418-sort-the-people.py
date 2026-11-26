class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        
        pairs=list(zip(names,heights))
        ans = sorted(pairs, key=lambda x: x[1], reverse=True)

        result=[]
        for pairs in ans:
            result.append(pairs[0])

        return result
            