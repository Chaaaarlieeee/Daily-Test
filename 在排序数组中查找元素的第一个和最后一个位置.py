class Solution:
    def search(self,nums:List[int],target:int):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]>=target:
                right=mid-1
            else:
                left=mid+1
        return left

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a=self.search(nums,target)
        if not nums:
            return[-1,-1]
        if a==len(nums) or nums[a]!=target:
            return[-1,-1]
        b=self.search(nums,target+1)-1
        return [a,b]