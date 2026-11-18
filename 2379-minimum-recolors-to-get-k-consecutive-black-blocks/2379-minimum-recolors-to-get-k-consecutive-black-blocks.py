class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        window = blocks[:k]
        count = window.count("W")
        mincount = count

        for i in range(k, len(blocks)):
            if blocks[i] == "W":
                count = count + 1

            if blocks[i-k] == "W":
                count = count - 1

            mincount = min(mincount, count)

        return mincount