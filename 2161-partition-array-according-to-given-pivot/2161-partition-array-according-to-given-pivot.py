class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small=[]
        greater=[]
        eq=[]
        for i in range(len(nums)):
            if nums[i]<pivot:
                small.append(nums[i])
            elif nums[i]>pivot:
                greater.append(nums[i])
            else:
                eq.append(nums[i])
        return small+eq+greater
        