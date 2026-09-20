class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        res=0
        for ch in s:
            res+=abs(s.find(ch)-t.find(ch))
        return res
        