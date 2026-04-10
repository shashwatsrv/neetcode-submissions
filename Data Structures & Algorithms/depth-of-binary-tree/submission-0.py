# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stk=[[root,1]]
        res=0

        while stk:
            node,dep=stk.pop()

            if node:
                res=max(res,dep)
                stk.append([node.left,dep+1])
                stk.append([node.right,dep+1])

        return res

        