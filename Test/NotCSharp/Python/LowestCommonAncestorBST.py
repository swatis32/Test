# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/submissions/
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root
        # p can be smaller or bigger than q, so need to check both conditions
        if (p.val <= root.val <= q.val) or (q.val <= root.val <= p.val):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if not left:
            return right
        if not right:
            return left
        return None