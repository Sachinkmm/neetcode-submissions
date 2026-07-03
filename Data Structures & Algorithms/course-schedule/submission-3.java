class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] inDegree = new int[numCourses];
        List<List<Integer>> adj = new ArrayList<>();

        for (int i = 0; i < numCourses; i++) {
            adj.add(new ArrayList<>());
        }

        for (int[] preq : prerequisites) {
            adj.get(preq[1]).add(preq[0]);
            inDegree[preq[0]] += 1;
        }

        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) {
                q.offer(i);
            }
        }
        int finish = 0;

        while (!q.isEmpty()) {
            int node = q.poll();
            finish += 1;
            for (int nbr : adj.get(node)) {
                inDegree[nbr] -= 1;
                if (inDegree[nbr] == 0) {
                    q.offer(nbr);
                }
            }
        }
        return finish == numCourses;
    }
}
