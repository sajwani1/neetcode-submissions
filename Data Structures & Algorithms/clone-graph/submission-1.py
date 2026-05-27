"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Create a hashmap of old nodes mapped to cloned nodes
        cloned = {}

        def dfs(node):
            # If the node has already been cloned,
            # just return it
            if node in cloned:
                return cloned[node]

            # Otherwise, create a new node with the 
            # original node's value
            copy = Node(node.val)
            # Add this new node to the hashmap
            cloned[node] = copy

            # Recursively go through all the neighbors of the node
            # and add them to the list of neighbors of the 
            # cloned node
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            # Return the copied node which now has all the 
            # neighbors attached as well
            return copy

        # Start the dfs on the node we are given
        return dfs(node) if node else None

        # Time Complexity: O(V + E)
        # Space Complexity: O(V)

        