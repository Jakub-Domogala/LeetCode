# Time Complexity:   O(n)
# Memory Complexity: O(1)

from typing import Optional

from utilities.ListNode import ListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_size(node):
            counter = 0
            while node:
                node = node.next
                counter += 1
            return counter

        def get_nth(node, n):
            counter = 1
            while counter < n:
                node = node.next
                counter += 1
            return node

        size = get_size(head)
        return get_nth(head, size // 2 + 1)


arr = [1, 2, 3, 4, 5, 6]
lst = ListNode().arr2list(arr)
print(lst)
print(Solution().middleNode(lst))
