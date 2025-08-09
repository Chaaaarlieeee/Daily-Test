class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


#v2
class Solution:
    def findmin(self,nums:list):
        l=0
        r=len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]<nums[-1]:
                r=mid
            else:
                l=mid+1
        return l


    def find(self, nums: list, l, r, target):
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1


    def search(self, nums: list[int], target: int) -> int:
        i = self.findmin(nums)
        if target > nums[-1]:
            return self.find(nums, 0, i - 1, target)
        else:
            return self.find(nums, i, len(nums) - 1, target)

