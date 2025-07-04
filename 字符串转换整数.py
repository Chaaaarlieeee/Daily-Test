# #v1
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        
        index = 0
        sign = 1
        result = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1
        
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN
            result = result * 10 + digit
            index += 1
        
        return sign * result

#v2 leetcode题解状态机
max_=2**31-1
min_=-2**31
class state_machine:
    def __init__(self):
        self.ans=0
        self.sign=1
        self.state="start"
        self.stop=False
        self.table={
            "start":["start","signed","in_number","end"],
            "signed":["end","end","in_number","end"],
            "in_number":["end","end","in_number","end"],
            "end":["end","end","end","end"],
        }
    def find(self,c):
        if c.isspace():
            return 0
        if c=="+"or c=="-":
            return 1
        if c.isdigit():
            return 2
        return 3
    def get(self,c):
        self.state=self.table[self.state][self.find(c)]
        if self.state=="in_number":
            self.ans=self.ans*10+int(c)
            if self.ans>=max_ or self.ans<=min_:
                self.ans= min(self.ans,max_) if self.sign==1 else min(self.ans,-min_)
                self.stop=True
        elif self.state=="signed":
            self.sign=1 if c=="+" else -1
        elif self.state=="end":
            self.stop=True
        return self.stop
class Solution:
    def myAtoi(self, str: str) -> int:
        ma=state_machine()
        for c in str:
            if ma.get(c):
                break
        return ma.ans*ma.sign

a=Solution()
print(a.myAtoi("42"))

#v3
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()                      # 删除首尾空格
        if not s: return 0                   # 字符串为空则直接返回
        res, i, sign = 0, 1, 1
        int_max, int_min, bndry = 2 ** 31 - 1, -2 ** 31, 2 ** 31 // 10
        if s[0] == '-': sign = -1            # 保存负号
        elif s[0] != '+': i = 0              # 若无符号位，则需从 i = 0 开始数字拼接
        for c in s[i:]:
            if not '0' <= c <= '9' : break     # 遇到非数字的字符则跳出
            if res > bndry or res == bndry and c > '7': return int_max if sign == 1 else int_min # 数字越界处理
            res = 10 * res + ord(c) - ord('0') # 数字拼接
        return sign * res

