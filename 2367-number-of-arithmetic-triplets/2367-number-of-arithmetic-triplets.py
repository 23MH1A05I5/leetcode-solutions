class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n=len(nums)
        count=0
        j=1
        k=2
        for i in range(n):
            while j<n and nums[j]-nums[i]<diff:
                j+=1
            if j==n:
                break
            while k<n and nums[k]-nums[j]<diff:
                k+=1
            if k<n and nums[j]-nums[i]==diff and nums[k]-nums[j]==diff:
                count+=1
        return count
        
        