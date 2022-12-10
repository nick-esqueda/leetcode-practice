class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> adjList = createAdjList(numCourses, prerequisites);
        // System.out.println(adjList);
        
        Set<Integer> visited = new HashSet<>();
        
        for (int course = 0; course < numCourses; ++course) {
            if (hasCycle(course, new HashSet<>(), visited, adjList)) {
                return false;
            } 
        }
        
        return true;
    }
    
    private boolean hasCycle(int course, Set<Integer> currPath, Set<Integer> visited, Map<Integer, List<Integer>> adjList) {
        if (currPath.contains(course)) {
            return true;
        }
        if (visited.contains(course)) {
            return false;
        }
        
        currPath.add(course);
        visited.add(course);
        
        for (int prereq : adjList.get(course)) {
            if (hasCycle(prereq, currPath, visited, adjList)) {
                return true;
            }
        }
        
        currPath.remove(course);
        return false;
    }
    
    private Map<Integer, List<Integer>> createAdjList(int numCourses, int[][] edgeList) {
        Map<Integer, List<Integer>> adjList = new HashMap<>();
        
        for (int course = 0; course < numCourses; ++course) {
            adjList.put(course, new ArrayList<>());
        }
        
        for (int[] edge : edgeList) {
            int a = edge[0], b = edge[1];
            adjList.get(a).add(b);
        }
        
        return adjList;
    }
}