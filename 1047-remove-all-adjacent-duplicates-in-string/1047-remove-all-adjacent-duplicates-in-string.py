class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans = []
        for i in range(len(s)):
            if ans and s[i]==ans[-1]:
                ans.pop()
            else:
                ans.append(s[i])
        return "".join(ans)

        # while True:
        #     deleated=False
        #     for i in range(len(s)-1):
        #         if s[i]==s[i+1]:
        #             s=s[:i]+s[i+2:]          bruit force
        #             deleated=True
        #             break
        #     if deleated==False:
        #         return s        