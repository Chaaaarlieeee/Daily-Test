#v1
class Solution:
    def romanToInt(self, s: str) -> int:
        n=len()
        s=list()
        value=0
        skip=False
        hashtable=dict(I=1,V=5,X=10,L=50,C=100,D=500,M=1000,IV=4,IX=9,XL=40,XC=90,CD=400,CM=900)
        for i in range(n):
            if skip == True:
                skip=False
                continue
            else:
                if i+1<n:
                    if ([i]+s[i+1]) in hashtable:
                        value=value+hashtable[[i]+s[i+1]]
                        skip=True
                    else:
                        value=value+hashtable[[i]]
                else:
                    value=value+hashtable[[i]]
        return value

#v2
class Solution:
    def romanToInt(self, s: str) -> int:
        hashtable = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                    'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        value = 0
        skip = False
        
        for i in range(len()):
            if skip:
                skip = False
                continue
            
            if i + 1 < len() and[i:i+2] in hashtable:
                value += hashtable[[i:i+2]]
                skip = True
            else:
                value += hashtable[[i]]
                
        return value
#v3
class Solution:

    SYMBOL_VALUES = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def romanToInt(self, s: str) -> int:
        ans = 0
        n = len()
        for i, ch in enumerate():
            value = Solution.SYMBOL_VALUES[ch]
            if i < n - 1 and value < Solution.SYMBOL_VALUES[[i + 1]]:
                ans -= value
            else:
                ans += value
        return ans

