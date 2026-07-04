class Solution {
    public boolean validTree(int n, int[][] edges) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }

        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }

        Set<Integer> visit = new HashSet<>();
        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{0, -1});
        visit.add(0);

        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int u = curr[0];
            int p = curr[1];
            for (int nbr : adj.get(u)) {
                if (nbr == p) {
                    continue;
                }
                if (visit.contains(nbr)) {
                    return false;
                }
                visit.add(nbr);
                q.offer(new int[]{nbr, u});
            }
        }
        return visit.size() == n;
    }
}
