class Solution:
    def minSwaps(self, s: str) -> int:
        stack=[]
        swaps=0
        for ch in s:
            if ch=='[':
                stack.append(ch)
            else:
                if stack:
                    stack.pop()
                else:
                    swaps+=1
                    stack.append('[')
        return swaps
        