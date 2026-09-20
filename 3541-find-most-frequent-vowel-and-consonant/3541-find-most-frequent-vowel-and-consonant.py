class Solution:
    def maxFreqSum(self, s: str) -> int:
        v=0
        c=0
        d="".join(set(s))
        for ch in d:
            if ch in "aeiou":
                v=max(v,s.count(ch))
            else:
                c=max(c,s.count(ch))
        return v+c


        