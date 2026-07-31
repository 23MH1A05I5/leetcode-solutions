class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            res=0
            while 0<nums[i]:
                
                res+=nums[i]%10
                nums[i]=nums[i]//10
            nums[i]=res
        return min(nums)
        