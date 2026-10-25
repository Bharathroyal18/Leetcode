class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        a1=bin(a)[2:]
        b1=bin(b)[2:]
        count1=0
        for i in a1:
            if i=="1":
                count1=count1+1
        count2=0
        for i in b1:
            if i=="1":
                count2=count2+1
        if count1>=count2:
            score=count1*count2
        else:
            score=count2//count1
        return score