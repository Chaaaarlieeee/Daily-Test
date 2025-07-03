import math
class Solution:
    def reverse(self, x: int) -> int:
        value=0
        a=0
        if x==0:
            return x
        if x<0:
            x=-x
            while x!=0:
                a=x%10
                x=x//10
                value=value*10+a
            if -value<(-math.pow(2,31)):
                return 0
            return -value
        else:
            while x!=0:
                a=x%10
                x=x//10
                value=value*10+a
            if value>(math.pow(2,31)-1):
                return 0
            return value