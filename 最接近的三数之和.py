class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        value=10**10
        total=0
        nums.sort()
        my_set=set(nums)
        if len(my_set)==1:
            return nums[0]*3
        if not nums:
            return target
        if nums[0]>target:
            return nums[0]+nums[1]+nums[2]
        for i,j in enumerate(nums):
            left,right=i+1,len(nums)-1
            while left<right and right<len(nums):
                if abs(target-nums[i]-nums[left]-nums[right])<value:
                    value=abs(target-nums[i]-nums[left]-nums[right])
                    total=nums[i]+nums[left]+nums[right]
                if (target-nums[i]-nums[left]-nums[right])==0:
                    return total
                elif (target-nums[i]-nums[left]-nums[right])>0:
                    left+=1
                elif (target-nums[i]-nums[left]-nums[right])<0:
                    right-=1

        return total
a=Solution()
print(a.threeSumClosest([-100,-98,-2,-1],-101))