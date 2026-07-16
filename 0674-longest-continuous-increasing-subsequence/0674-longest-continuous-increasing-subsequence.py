class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        maxlen=1
        count=1
        for i in range(1,len(nums)):
            
            if nums[i-1]<nums[i]:
                count+=1
            else:
                count=1
            maxlen=max(maxlen,count)
        return maxlen
            

            

        