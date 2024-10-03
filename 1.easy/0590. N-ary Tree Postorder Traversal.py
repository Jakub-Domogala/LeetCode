# Time Complexity:   O(n)
# Memory Complexity: O(n)

# To better understand this solution head to similiar problem 0144 which includes visualisations

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        def dive(node):
            nonlocal result
            if node is None:
                return
            for c in node.children:
                dive(c)
            result += [node.val]
        dive(root)
        return result
