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