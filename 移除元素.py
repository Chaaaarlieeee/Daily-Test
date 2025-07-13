#v1
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = list()  
        for i in nums:
            if i != val:
                a.append(i) 
        nums[:] = a 
        n = len(a)
        return n 