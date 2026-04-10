"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        otc={None:None}

        curr=head

        while curr:
            copy=Node(curr.val)
            otc[curr]=copy
            curr=curr.next
        curr=head
        while curr:
            copy=otc[curr]
            copy.next=otc[curr.next]
            copy.random=otc[curr.random]
            curr=curr.next
        return otc[head]
        