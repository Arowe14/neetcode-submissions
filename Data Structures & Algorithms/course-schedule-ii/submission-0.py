class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        preMap = {i: [] for i in range(numCourses)}

        for c, p in prerequisites: # Hashmap with list of prereqs for that course
            preMap[c].append(p)

        
        visited = set()
        added = set()
        def dfs(crs):
            print(crs)
            if crs in visited:
                print("In Visited")
                return False

            if preMap[crs] == []:
                if crs not in added:
                    added.add(crs)
                    res.append(crs)
                return True
            
            visited.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
                
            visited.remove(crs)
            preMap[crs] = []
            added.add(crs)
            res.append(crs)
            print("Added ", crs)
            return True

        
        for n in range(numCourses): 
            if not dfs(n):
                return []

        for i in range(numCourses): # Add all courses that may not have been featured in prereqs
            if i not in added:
                res.append(i)
                added.add(i)

        return res