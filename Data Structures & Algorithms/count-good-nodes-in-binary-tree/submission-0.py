# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        curr = root
        maxx = curr.val
        goodNodes = 0
        goodNodes = self.dfs(curr, maxx, goodNodes)
        return goodNodes


    def dfs(self, curr, maxx, goodNodes):
        if not curr:
            return goodNodes
        if curr.val >= maxx:
            maxx = curr.val
            goodNodes += 1
        goodNodes = self.dfs(curr.right, maxx, goodNodes)
        goodNodes = self.dfs(curr.left, maxx, goodNodes)

        return goodNodes

        
        