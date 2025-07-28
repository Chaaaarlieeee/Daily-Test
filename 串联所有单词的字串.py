class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        n=0
        current=str()
        differ=Counter()
        index=list()
        differ=Counter(words)
        while n+len(words[0])*len(words)<=len(s):
            i=n
            for _ in range(len(words)):
                current=s[i:i+len(words[0])]
                if current in differ:
                    differ[current]-=1
                current=str()
                i+=len(words[0])
            k=True
            for j in differ:
                if differ[j]!=0:
                    k=False
                    break
            if k:
                index.append(i-len(words)*len(words[0]))
            differ=Counter(words)
            n+=len(words[0])
        return index




            
            

a=Solution()
print(a.findSubstring("barfoothefoobarman",["foo","bar"]))