class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        i = 0
        j = 0
        ans = []

        while len(firstList) > i and len(secondList) > j:
            
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            if start <= end:
                ans.append([start, end])

            if firstList[i][1] > secondList[j][1]:
                j = j + 1
            else:
                i = i + 1

        return ans