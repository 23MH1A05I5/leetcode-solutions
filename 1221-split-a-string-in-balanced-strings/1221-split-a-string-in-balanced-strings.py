class Solution:
    def balancedStringSplit(self, s: str) -> int:
        bal=0
        count=0
        for ch in s:
            if ch=="R":
                bal+=1
            else:
                bal-=1
            if bal==0:
                count+=1
        return count
        