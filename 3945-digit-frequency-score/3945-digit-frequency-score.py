class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        count={}
        res=0
        for ch in str(n):
            count[int(ch)]=count.get(int(ch),0)+1
        for key,values in count.items():
            res+=key*values
        return res