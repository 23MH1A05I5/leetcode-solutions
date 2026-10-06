class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]: 
        result=set()
        freq=[0]*10
        for i in digits:
            freq[i]+=1
        def backtrack(count,num):
            if count==3:
                if num%2==0:
                    result.add(num)
                return
            for d in range(10):
                if freq[d]==0:
                    continue
                if count==0 and d==0:
                    continue
                freq[d]-=1
                backtrack(count+1,num*10+d)

                freq[d]+=1
        backtrack(0,0)
        return sorted(result)

        
        