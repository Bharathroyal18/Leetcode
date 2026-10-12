class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        n=list(s)
        left=0
        right=k-1
        while left<=right:
            n[left],n[right]=n[right],n[left]
            left=left+1
            right=right-1

        return "".join(n)