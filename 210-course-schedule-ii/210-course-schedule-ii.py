class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        0 4 if there are numCourses = 5
        if you get the topological order (from "starting" nodes to "ending nodes"), you can return the reverse of that order
        if you have to take a course to take another course, but that couse requires the first as a prereq, that's a cycle
        need to be able to detect cycles - return [] if cycle is detected
        you'll notice there is a cycle if there are nodes in the parent count list you make that are > 0
        this is because you would have exited early because the stack was empty, since something had 2 parents, but you couldn't get to the 2nd
        """
        adj = { i: [] for i in range(numCourses) }
        for a, b in prerequisites:
            adj[a].append(b)

        parent_counts = { i: 0 for i in adj }
        for parent in adj:
            for child in adj[parent]:
                parent_counts[child] += 1
     
        sta = [course for course in parent_counts if parent_counts[course] == 0]
        top_order = []
        while sta:
            course = sta.pop()
            top_order.append(course)
            for prereq in adj[course]:
                parent_counts[prereq] -= 1
                if parent_counts[prereq] == 0:
                    sta.append(prereq)
      
        for course in parent_counts:
            if parent_counts[course] > 0:
                return []
        return top_order[::-1]