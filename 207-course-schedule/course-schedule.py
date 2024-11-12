class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList={}
        for i in range(numCourses):
            adjList[i]=[]
        for crs,pre in prerequisites:
            adjList[crs].append(pre)
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if adjList[crs]==[]:
                return True
            visited.add(crs)
            for i in adjList[crs]:
                if not dfs(i): 
                    return False
            visited.remove(crs)
            adjList[crs]=[]
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True