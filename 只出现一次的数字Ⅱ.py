#v1
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        table=dict()
        for i in nums:
            if i in table:
                table[i]=table[i]+1
            else:
                table[i]=1
        for key,value in table.items():
            if value==1:
                return int(key)
#v2
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        ans = [num for num, occ in freq.items() if occ == 1][0]
        return ans
