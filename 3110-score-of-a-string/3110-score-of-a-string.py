class Solution:
    def scoreOfString(self, s: str) -> int:
        res=list(s)
        ans=0
        for i in range(len(res)-1):
            ans+=abs(ord(res[i])-ord(res[i+1]))
        return ans
