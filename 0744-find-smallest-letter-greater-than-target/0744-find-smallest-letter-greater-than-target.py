class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        for i in range(len(letters)):
            if letters[i] > target:
                return letters[i]

        return letters[0]


# class Solution:
#     def nextGreatestLetter(self, letters: List[str], target: str) -> str:
#         left=0
#         right=len(letters)-1
#         while left<=right:
#             i=(left+right)//2
#             if letters[i] <= target:
#                 left+= 1
#             else:
#                 right-=1
#         return letters[left%len(letters)]
        