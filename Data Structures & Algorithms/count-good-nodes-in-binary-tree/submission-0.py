# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 0
        def dfs(root, val):
            nonlocal ans
            if not root:
                return
            if root.val >= val:
                ans += 1
            dfs(root.left, max(root.val, val))
            dfs(root.right, max(root.val, val))
        dfs(root, -101)
        return ans

        