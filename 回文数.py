#v1:24ms,17.45MB
class Solution:
    def isPalindrome(self, x: int) -> bool:
        arr1=list()
        arr2=list()
        if x<0:
            return False
        while x!=0:
            a=x%10
            x=x//10
            arr1.append(a)
        arr2=arr1.copy()
        arr2.reverse()
        for i,num in enumerate(arr2):
            if num!=arr1[i]:
                return False
        return True
#v2:2ms,17.54MB
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0):
            return False
        
        reverse=0
        while(x>reverse):
            reverse=reverse*10+x%10
            x=x//10
        
        return x==reverse or x==reverse//10
        