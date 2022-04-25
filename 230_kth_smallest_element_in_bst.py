# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        k, val = self.kth(root, k)
        if not k:
            return val
        return None

    def kth(self, root, k):
        if not root or not k:
            return k, None
        k, val = self.kth(root.left, k)
        if not k:
            return k, val
        else:
            k = k - 1
            if not k:
                return k, root.val
            k, val = self.kth(root.right, k)
            return k, val
