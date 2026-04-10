# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stk=[]
        def dfs(node):
            nonlocal stk
            if not node:
                return None
            dfs(node.left)
            stk.append(node.val)
            dfs(node.right)
        dfs(root)
        
        return stk[k-1]


        