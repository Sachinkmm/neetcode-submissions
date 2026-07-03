class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int[] inDegree = new int[numCourses];
        List<List<Integer>> adj = new ArrayList<>();

        for (int i = 0; i < numCourses; i++) {
            adj.add(new ArrayList<>());
        }

        for (int[] preq : prerequisites) {
            int u = preq[0], v = preq[1];
            adj.get(v).add(u);
            inDegree[u] += 1;
        }

        Queue<Integer> q = new LinkedList<>();
        // List<Integer> output = new ArrayList<>();
        int[] output = new int[numCourses];
        int finish = 0;

        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) {
                q.offer(i);
            }
        }

        while (!q.isEmpty()) {
            int node = q.poll();
            output[finish] = node;
            finish += 1;
            for (int v : adj.get(node)) {
                inDegree[v] -= 1;
                if (inDegree[v] == 0) {
                    q.offer(v);
                }
            }
        }
        if (finish == numCourses) {
            return output;
        }
        return new int[0];
    }
}
