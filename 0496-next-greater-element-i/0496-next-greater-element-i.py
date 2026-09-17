class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack=[]
        nxt={}
        for num in nums2:
            while stack and stack[-1]<num:
                pri=stack.pop()
                nxt[pri]=num
            stack.append(num)
        while stack:
            pri=stack.pop()
            nxt[pri]=-1
        ans=[]    
        for num in nums1:
            ans.append(nxt[num])
        return ans
            
        
        