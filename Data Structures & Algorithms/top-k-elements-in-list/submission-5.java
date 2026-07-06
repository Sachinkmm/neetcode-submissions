class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int n = nums.length;
        List<Integer>[] freq = new ArrayList[n + 1];
        Map<Integer, Integer> mp = new HashMap<>();

        for (int i = 0; i < freq.length; i++) {
            freq[i] = new ArrayList<>();
        }

        for (int i = 0; i < n; i++) {
            mp.merge(nums[i], 1, Integer::sum);
        }

        for (Map.Entry<Integer, Integer> it : mp.entrySet()) {
            int key = it.getKey();
            int val = it.getValue();
            freq[val].add(key);
        }

        int[] res = new int[k];
        int idx = 0;
        for (int i = freq.length - 1; i > 0 && idx < k; i--) {
            for (int num : freq[i]) {
                res[idx++] = num;
                if (idx == k) {
                    return res;
                }
            }
        }
        return res;
    }
}
