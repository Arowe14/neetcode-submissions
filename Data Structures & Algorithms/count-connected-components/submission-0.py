class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set() #visited

        adj = [[] for _ in range(n)] # Adjacency List
        for u, v in edges: # adj[u] is list of adjacent points v
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node): # DFS. Adds visited to visit
            for neighbor in adj[node]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    dfs(neighbor)

        res = 0
        for node in range(n): # Runs through new nodes.
        # Each time new node is found, increment res
            if node not in visit:
                visit.add(node)
                dfs(node)
                res += 1
        return res
