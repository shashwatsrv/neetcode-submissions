# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    
        def isSame(p,q):
            if not p and not q:
                return True
            if not p or not q or p.val!=q.val:
                return False
            return isSame(p.left,q.left) and isSame(p.right,q.right)

        def search(root,subRoot):
            if subRoot is None:
                return True
            if root is None:
                return False
            if isSame(root,subRoot):
                return True
            
            return search(root.left,subRoot) or search(root.right,subRoot)
        return search(root,subRoot)