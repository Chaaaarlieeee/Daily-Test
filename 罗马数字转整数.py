#v1
class Solution:
    def romanToInt(self, s: str) -> int:
        n=len(s)
        s=list(s)
        value=0
        skip=False
        hashtable=dict(I=1,V=5,X=10,L=50,C=100,D=500,M=1000,IV=4,IX=9,XL=40,XC=90,CD=400,CM=900)
        for i in range(n):
            if skip == True:
                skip=False
                continue
            else:
                if i+1<n:
                    if (s[i]+s[i+1]) in hashtable:
                        value=value+hashtable[s[i]+s[i+1]]
                        skip=True
                    else:
                        value=value+hashtable[s[i]]
                else:
                    value=value+hashtable[s[i]]
        return value

#v2
class Solution:
    def romanToInt(self, s: str) -> int:
        hashtable = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                    'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        value = 0
        skip = False
        
        for i in range(len(s)):
            if skip:
                skip = False
                continue
            
            if i + 1 < len(s) and s[i:i+2] in hashtable:
                value += hashtable[s[i:i+2]]
                skip = True
            else:
                value += hashtable[s[i]]
                
        return value