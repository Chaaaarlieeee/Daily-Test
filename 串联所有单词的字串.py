class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        n=0
        current=str()
        differ=Counter()
        index=list()
        differ=Counter(words)
        while n+len(words[0])*len(words)<=len():
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


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        m, n, ls = len(words), len(words[0]), len()
        for i in range(n):
            if i + m * n > ls:
                break
            differ = Counter()
            for j in range(m):
                word = s[i + j * n: i + (j + 1) * n]
                differ[word] += 1
            for word in words:
                differ[word] -= 1
                if differ[word] == 0:
                    del differ[word]
            for start in range(i, ls - m * n + 1, n):
                if start != i:
                    word = s[start + (m - 1) * n: start + m * n]
                    differ[word] += 1
                    if differ[word] == 0:
                        del differ[word]
                    word = s[start - n: start]
                    differ[word] -= 1
                    if differ[word] == 0:
                        del differ[word]
                if len(differ) == 0:
                    res.append(start)
        return res



            
            

a=Solution()
print(a.findSubstring("barfoothefoobarman",["foo","bar"]))
