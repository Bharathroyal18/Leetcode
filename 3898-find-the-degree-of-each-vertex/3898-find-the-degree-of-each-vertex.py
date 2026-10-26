class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ans = []

        for i in range(len(matrix)):
            val = 0

            for j in range(len(matrix[i])):
                val = val + matrix[i][j]

            ans.append(val)

        return ans