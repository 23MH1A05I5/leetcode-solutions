class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans=""
        for ch in words:
            res=0
            for c in ch:
                res+=weights[ord(c)-ord('a')]
            res=res%26
            ans+=chr(ord('z')-res)
        return ans




        