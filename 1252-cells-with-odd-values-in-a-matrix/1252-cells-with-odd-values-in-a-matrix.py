class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        matrix = [[0] * n for _ in range(m)]

        for r, c in indices:
            for j in range(n):
                matrix[r][j] += 1

            for i in range(m):
                matrix[i][c] += 1

        count = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] % 2 != 0:
                    count += 1

        return count