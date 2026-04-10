# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        qu=deque()
        qu.append((p,q))

        while qu:
            node_p,node_q=qu.popleft()
            if node_p and node_q:
                qu.append((node_p.left,node_q.left))
                qu.append((node_p.right,node_q.right))
            if not node_p and not node_q:
                continue
            if not node_p or not node_q or node_p.val!=node_q.val:
                return False   

        return True
        
        