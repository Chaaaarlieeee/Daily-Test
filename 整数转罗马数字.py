#v1
class Solution:
    def intToRoman(self, num: int) -> str:
        head1=None
        head2=None
        for i in [1,4,5,9,10,40,50,90,100,400,500,900,1000]:
            head1 = ListNode(i,head1)
        for i in ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]:
            head2 = ListNode(i,head2)
        value=str()
        while num>0:
            if num-head1.val < 0:
                head1=head1.next
                head2=head2.next
            if num-head1.val >=0:
                value=value+head2.val
                num=num-head1.val
        return value
#v2
class Solution:
    def intToRoman(self, num: int) -> str:
            VALUE_SYMBOLS = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
        ]
            value = str()
            for val,rom in VALUE_SYMBOLS:
                while num>=val:
                    num-=val
                    value=value+rom
                if num==0:
                    break
            return value


            
