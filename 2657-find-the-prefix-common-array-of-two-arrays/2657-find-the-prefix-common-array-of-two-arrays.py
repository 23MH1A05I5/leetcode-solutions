class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        count=0
        freq={}
        res=[0]*len(A)
        for i in range(len(A)):
            freq[A[i]]=freq.get(A[i],0)+1
            if freq[A[i]]==2:
                count+=1
            freq[B[i]]=freq.get(B[i],0)+1
            if freq[B[i]]==2:
                count+=1
            res[i]=count
        return res

        