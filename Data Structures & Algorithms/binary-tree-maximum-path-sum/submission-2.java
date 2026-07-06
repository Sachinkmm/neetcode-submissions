/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public int maxPathSum(TreeNode root) {
        int[] res = new int[1];
        res[0] = root.val;
        dfs(root, res);
        return res[0];
    }

    public int dfs(TreeNode root, int[] res) {
        if (root == null) {
            return 0;
        }

        int leftMax = Math.max(0, dfs(root.left, res));
        int rightMax = Math.max(0, dfs(root.right, res));
        res[0] = Math.max(res[0], root.val + leftMax + rightMax);

        return root.val + Math.max(leftMax, rightMax);
    }
}
