class Solution:
    def stringHash(self, s: str, k: int) -> str:
        res=[]
        for i in range(0,len(s),k):
            sub=s[i:i+k]
            ans=sum(ord(char)-ord("a") for char in sub)
            res+=chr(ord("a")+ ans%26)
        return "".join(res)
            


        
        