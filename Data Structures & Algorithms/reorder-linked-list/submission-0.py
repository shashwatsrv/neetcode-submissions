# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head.next
        while fast and fast.next: 
            #Even and odd case
            slow=slow.next
            fast=fast.next.next

        #Reversal
           
        second=slow.next
        prev=slow.next=None
        while second:
             #second part will always be <= first part of the list
             tmp=second.next
             second.next=prev
             prev=second
             second=tmp
        
        #Merging 
        first,second=head,prev
        while second:
            tmp1,tmp2=first.next,second.next
            first.next=second
            second.next=tmp1
            first,second=tmp1,tmp2
        