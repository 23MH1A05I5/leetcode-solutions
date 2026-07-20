class Solution:
    def reverseDegree(self, s: str) -> int:
        ans=0
        for i in range(len(s)):
            ch=s[i]
            reverse=ord('z')-ord(ch)+1
            ans+=reverse*(i+1)
        return ans

        