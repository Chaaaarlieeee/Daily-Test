class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 0:
            return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans
a=Solution()
print(a.generateParenthesis(3))