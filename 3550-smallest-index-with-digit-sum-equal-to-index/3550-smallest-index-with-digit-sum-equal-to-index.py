class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            ans=0
            while nums[i]:
                ans+=nums[i]%10
                nums[i]=nums[i]//10
            if ans==i:
                return i
        else:
            return -1
                
        