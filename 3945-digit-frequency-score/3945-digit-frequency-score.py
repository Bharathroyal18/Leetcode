class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        s=str(n)
        a=list(s)
        d={}
        for i in range(len(a)):
            if a[i] in d:
                d[a[i]]=d[a[i]]+1
            else:
                d[a[i]]=1
        total=0
        for key in d:
            total=total+int(key)*d[key]
        return total

        