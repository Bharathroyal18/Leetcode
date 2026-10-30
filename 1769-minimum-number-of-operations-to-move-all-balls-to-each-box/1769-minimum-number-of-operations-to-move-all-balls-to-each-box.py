class Solution:
    def minOperations(self, boxes: str) -> list[int]:

        ans = []

        for i in range(len(boxes)):
            operations = 0

            for j in range(len(boxes)):
                if boxes[j] == '1':
                    operations = operations +  abs(i - j)

            ans.append(operations)
        
        return ans