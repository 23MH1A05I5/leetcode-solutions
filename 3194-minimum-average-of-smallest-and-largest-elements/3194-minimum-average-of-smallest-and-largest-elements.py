class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        left=0
        right=len(nums)-1
        res=[]
        while left<right:
            r=(nums[left]+nums[right])/2
            res.append(r)
            left+=1
            right-=1
        return min(res)

        