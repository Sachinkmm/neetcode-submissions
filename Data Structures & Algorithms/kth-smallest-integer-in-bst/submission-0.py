# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        def inorder(root):
            nonlocal k, ans
            if not root or k == 0:
                return
            inorder(root.left)
            k -= 1
            if (k == 0):
                ans = root.val
                return
            inorder(root.right)
        inorder(root)
        return ans