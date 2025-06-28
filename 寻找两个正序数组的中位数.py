#v1:合并列表后计算
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        a=nums1
        n=len(a)
        if (n/2)==(n//2):
            result=(a[int(n/2-1)]+a[int(n/2)])/2
            return result
        else:
            result=a[int(((n+1)/2)-1)]
            return result
        

        