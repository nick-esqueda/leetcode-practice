class Solution {
    public int countComponents(int n, int[][] edges) {
        Map<Integer, List<Integer>> adjList = createAdjList(n, edges);
        Set<Integer> visited = new HashSet<>();
        int componentCount = 0;
        
        for (int node : adjList.keySet()) {
            if (!visited.contains(node)) {
                exploreComponent(node, visited, adjList);
                ++componentCount;
            }
        }
        
        return componentCount;
    }
    
    private void exploreComponent(int node, Set<Integer> visited, Map<Integer, List<Integer>> adjList) {
        if (visited.contains(node)) {
            return;
        }
        
        visited.add(node);
        for (int neighbor : adjList.get(node)) {
            exploreComponent(neighbor, visited, adjList);
        }
    }
    
    private Map<Integer, List<Integer>> createAdjList(int numNodes, int[][] edges) {
        Map<Integer, List<Integer>> adjList = new HashMap<>();
        
        for (int node = 0; node < numNodes; ++node) {
            adjList.put(node, new ArrayList<>());
        }
        
        for (int[] edge : edges) {
            int a = edge[0], b = edge[1];
            
            adjList.get(a).add(b);
            adjList.get(b).add(a);
        }
        
        return adjList;
    }
}