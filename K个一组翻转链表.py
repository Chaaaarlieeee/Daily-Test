# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head:ListNode,tail:ListNode):
        p=head
        prev=tail.next
        while prev!=tail:
            nex=p.next
            p.next=prev
            prev=p
            p=nex
        return tail,head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        hair=dummy
        tail=hair
        pre=hair
        while head:
            for i in range(k):
                tail=tail.next
                if not tail:
                    return hair.next
            head,tail=self.reverse(head,tail)
            pre.next=head
            pre=tail
            head=tail.next            
        return hair.next

        
    
        