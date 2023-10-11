# Time Complexity:   O(O(E))
# Memory Complexity: O(O(E))
# Where E is amount of edges


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
from collections import defaultdict


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        new_nodes = {}

        def dive(node):
            if node in new_nodes:
                return new_nodes[node]
            new_nodes[node] = Node(node.val)
            new_nodes[node].neighbors = [dive(nei) for nei in node.neighbors]
            return new_nodes[node]

        return dive(node) if node else None
