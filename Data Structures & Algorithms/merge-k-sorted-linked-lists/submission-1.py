# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        nodes=[]
        for i in lists:
            while i:
                nodes.append(i.val)
                i=i.next
        nodes.sort()

        op=ListNode(0)
        curr=op
        for node in nodes:
            curr.next=ListNode(node)
            curr=curr.next
        return op.next

        