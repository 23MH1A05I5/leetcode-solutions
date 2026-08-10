class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        nums.sort()
        left=0
        right=n-1
        arr=[]
        while left<=right:
            mid=left+ (right-left)//2
            if nums[mid]==target:
                arr.append(mid)
                i=mid-1
                while i>=0 and nums[i]==target:
                    arr.append(i)
                    i=i-1
                i=mid+1
                while i<n and nums[i]==target:
                    arr.append(i)
                    i+=1
                break
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return sorted(arr)

        