class Solution:
    def longestValidParentheses(self, s: str) -> int:
        lable=list()
        tm=[0]*len(s)
        cur=0
        maxl=0
        for i,j in enumerate(s):
            if j=="(":
                lable.append(i)
            else:
                if lable:
                    k=lable.pop()
                    tm[i]=1
                    tm[k]=1
        
        for num in tm:
            if num:
                cur+=1
            else:
                maxl=max(maxl,cur)
                cur=0
        maxl=max(maxl,cur)
        return maxl