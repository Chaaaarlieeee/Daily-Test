class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right=0,0
        occ=set()
        ans=0
        n=len(s)
        while right<n:
            if  s[right] in occ:
                occ.remove(s[left])
                left+=1
            else:
                occ.add(s[right])
                right+=1
                ans=max(ans,right-left)
        return ans