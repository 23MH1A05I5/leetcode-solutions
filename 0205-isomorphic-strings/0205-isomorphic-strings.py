class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        count1={}
        count2={}
        for i in range(len(s)):
            ch1=s[i]
            ch2=t[i]
            if ch1 in count1:
                if count1[ch1]!=ch2:
                    return False
            else:
                count1[ch1]=ch2
            if ch2 in count2:
                if count2[ch2]!=ch1:
                    return False
            else:
                count2[ch2]=ch1
        return True
        