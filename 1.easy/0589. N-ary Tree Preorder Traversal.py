# Time Complexity:   O(n)
# Memory Complexity: O(n)

# To better understand this solution head to problem 0144 which includes visualisations

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        def dive(node):
            nonlocal result
            if node is None:
                return
            result += [node.val]
            for c in node.children:
                dive(c)
        dive(root)
        return result
