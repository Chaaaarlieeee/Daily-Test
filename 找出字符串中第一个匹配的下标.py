class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hay=[]
        nee=[]
        for i in range(len(haystack)):
            hay.append(haystack[i])
        for i in range(len(needle)):
            nee.append(needle[i])
        
        for i in range(len(haystack)):
            judge=i
            j=0
            while i<len(haystack) and j<len(needle):
                if hay[i]!=nee[j]:
                    judge=-1
                    break
                i+=1
                j+=1
            if judge!=-1:
                return judge
        return -1
a=Solution()
print(a.strStr("mississippi","issipi"))