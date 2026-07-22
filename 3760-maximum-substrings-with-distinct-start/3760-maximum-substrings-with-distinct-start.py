class Solution:
    def maxDistinct(self, s: str) -> int:
        count={}
        for ch in s:
            count[ch]=count.get(ch,0)+1
        return len(count)
        