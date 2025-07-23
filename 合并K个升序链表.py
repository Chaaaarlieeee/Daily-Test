class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        table = []
        if not lists:
            return None
        for head in lists:
            while head:
                table.append(head.val)
                head = head.next
        
        table.sort()
        dummy = ListNode(0)
        curr = dummy
        for val in table:
            curr.next = ListNode(val)
            curr = curr.next
        
        return dummy.next

