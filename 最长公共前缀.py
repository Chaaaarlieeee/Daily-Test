#v1
class Solution:
    def check_identical_elements_2(self,lst):
        return len(set(lst)) == 1
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs)==1:
            return strs[0]
        for i in strs:
            if i=="":
                return ""
        table = ["" for _ in range((len(strs)))]
        shortest_string = min(strs, key=len)
        n=len(shortest_string)
        j=0
        while n>0:
            if self.check_identical_elements_2(table)!=True:
                    e=str(table[0])
                    e=e[:-1]
                    return e
            for i,s in enumerate(strs):
                table[i]=table[i]+s[j]
            j=j+1    
            n=n-1
        if self.check_identical_elements_2(table)!=True:
            e=str(table[0])
            e=e[:-1]
            return e
        else:return table[0]
#v2        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
                return strs[0][:i]
        
        return strs[0]

