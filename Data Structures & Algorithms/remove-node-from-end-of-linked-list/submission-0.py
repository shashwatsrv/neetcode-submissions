# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        last,slow=head,head
        size=1
        
        while last.next:
            last=last.next
            size+=1

        if n==size:
            return head.next

        req=size-n-1

        for i in range(req):
            slow=slow.next
        
        slow.next=slow.next.next

        return head
        


        