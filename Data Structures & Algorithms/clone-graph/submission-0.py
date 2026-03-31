"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited={}
        def dfs(old_node):
            if old_node in visited:
                return visited[old_node]
            copy = Node(old_node.val)
            visited[old_node] = copy
            for nbr in old_node.neighbors:
                copy.neighbors.append(dfs(nbr))
            
            return copy
        
        return dfs(node)