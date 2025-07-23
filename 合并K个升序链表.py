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

import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        dummy=ListNode(0)
        p=dummy
        head=[]
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(head,(lists[i].val,i))
                lists[i]=lists[i].next
        while head:
            val,idx=heapq.heappop(head)
            p.next=ListNode(val)
            p=p.next
            if lists[idx]:
                heapq.heappush(head,(lists[idx].val,idx))
                lists[idx]=lists[idx].next
        return dummy.next
