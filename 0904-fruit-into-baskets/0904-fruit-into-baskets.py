class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        maximum=0
        left=0
        d={}
        for right in range(len(fruits)):
            if fruits[right] in d:
                d[fruits[right]]=d[fruits[right]]+1
            else:
                d[fruits[right]]=1
            while len(d)>2:
                d[fruits[left]]=d[fruits[left]]-1
                
                if d[fruits[left]]==0:
                    del d[fruits[left]]
                left=left+1
            length=right-left+1
            maximum=max(maximum,length)
        return maximum
        