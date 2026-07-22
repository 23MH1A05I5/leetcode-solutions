class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        group={}
        ans=[]
        for num in nums:
            group[num]=group.get(num,0)+1
            row=group[num]-1
            if row==len(ans):
                ans.append([])
            ans[row].append(num)
        return ans
                 


