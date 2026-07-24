# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        #check the value at the current node
        #recurse on the left AND right subtrees because all of those values have to be the same too

        #if both end then return True (because you haven't returned false up to that point)
        #if one ends but the other doesnt, then they dont have the same structure

        if not p and not q: return True
        if not p or not q: return False

        if p.val != q.val: return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
