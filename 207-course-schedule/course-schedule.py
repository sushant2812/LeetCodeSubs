class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList={}
        for i in range(numCourses):
            adjList[i]=[]
        for crs,pre in prerequisites:
            adjList[crs].append(pre)
        visited=set()
        def dfs(crs):
            if crs in visited:
                return False ## Cycle is detected
            if adjList[crs]==[]:
                return True ##We can take that course
            visited.add(crs)
            for prereqs in adjList[crs]:
                if not dfs(prereqs):
                    return False
            visited.remove(crs)
            adjList[crs]=[]
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True