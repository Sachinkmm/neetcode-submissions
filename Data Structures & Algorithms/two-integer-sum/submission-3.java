class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int num1 = target - nums[i];
            if (map.containsKey(num1)) {
                return new int[] {map.get(num1), i};
            }
            map.put(nums[i], i);
        }
        return new int[] {};
    }
}
