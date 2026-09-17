class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack=[]
        ans=[]
        num=1
        for ch in pattern:
            stack.append(str(num))
            num+=1
            if stack and ch=='I':
                while stack:
                    ans.append(stack.pop())
        stack.append(str(num))
        while stack:
            ans.append(stack.pop())
        return ''.join(ans)
            

        