class Solution:
    def reverseByType(self, s: str) -> str:
        lett=[]
        spec=[]
        for ch in s:
            if ch.isalpha():
                lett.append(ch)
            else:
                spec.append(ch)
        lett.reverse()
        spec.reverse()
        ans=[]
        i=0
        j=0
        for ch in s:
            if ch.isalpha():
                ans.append(lett[i])
                i+=1
            else:
                ans.append(spec[j])
                j+=1
        return "".join(ans)


        