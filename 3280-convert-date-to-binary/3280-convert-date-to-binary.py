class Solution:
    def convertDateToBinary(self, date: str) -> str:
        val = date.split("-")
        ans = []
        for i in range(len(val)):
            ans.append(bin(int(val[i]))[2:])
        return "-".join(ans)