class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False
        table={")":"(","}":"{","]":"["}
        d=list()
        for i in s:
            if i in table and d:
                if d[-1]!=table[i]:
                    return False
                elif i in table and d[-1]==table[i]:
                    d.pop()
            else:
                d.append(i)
        return not d
a=Solution()
print(a.isValid("){"))