#v1
class Solution:
    def maxArea(self, height: List[int]) -> int:
        table=[]
        for i,j in enumerate(height):
            table.append([i,j])
        left=0
        right=0
        area=0
        current_area=0
        while left<=len(height):
            right=left+1
            while right<len(height):
                current_area=((right-left)*min(int(table[left][1]),int(table[right][1])))
                if current_area>area:
                    area=current_area
                right+=1
            left+=1
        return area
#v2
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        area=0
        while left!=right:
            if area<min(height[left],height[right])*(right-left):
                area=min(height[left],height[right])*(right-left)
            if height[left]<height[right]:
                left+=1
            elif height[left]>height[right]:
                right-=1
            else: left+=1
        return area
