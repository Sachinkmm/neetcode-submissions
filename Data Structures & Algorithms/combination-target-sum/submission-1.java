class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> tmp = new ArrayList<>();
        recur(nums.length - 1, target, nums, ans, tmp);
        return ans;
    }

    public void recur(int idx, int target, int[] nums, List<List<Integer>> ans, List<Integer> tmp) {
        if (target == 0) {
            ans.add(new ArrayList(tmp));
            return;
        }
        if (idx < 0) {
            return;
        }

        if (nums[idx] <= target) {
            tmp.add(nums[idx]);
            recur(idx, target - nums[idx], nums, ans, tmp);
            tmp.remove(tmp.size() - 1);
        }
        recur(idx - 1, target, nums, ans, tmp);
    }
}
