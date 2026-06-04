class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites: # Hashmap containing array of prereqs for preMap[crs]
            preMap[crs].append(pre)

        
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            
            if preMap[crs] == []: # crs was already checked
                return True
            
            visiting.add(crs)

            for pre in preMap[crs]: # For every pre of crs
                if not dfs(pre): # Check if that has cycle
                    return False
            
            visiting.remove(crs) # Remove if crs was already checked
            preMap[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True


