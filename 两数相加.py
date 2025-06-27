class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new=ListNode(0)
        head=new
        carry=0
        while l1 or l2 or carry:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0

            total=val1+val2+carry
            carry=total//10
            a=total%10
            head.next=ListNode(a)
            head=head.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        head=new.next
        return head