class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack=[]
        res=[]
        tar=0
        for i in range(1,n+1):
            res.append('Push')
            stack.append(i)
            if stack[-1]==target[tar]:
                tar+=1
            else:
                res.append('Pop')
                stack.pop()
            if stack==target:
                break
        return res
            
            