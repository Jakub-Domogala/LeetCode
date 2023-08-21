# Time Complexity:   O(n)
# Memory Complexity: O(1)
# Where n is max(len(list1), len(list2))

from typing import Optional
from utilities.ListNode import ListNode

class Solution(object):
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        result = ListNode()
        jr = result
        j1 = list1
        j2 = list2
        while True:
            if j1 is None:
                jr.next = j2
                return result.next
            if j2 is None:
                jr.next = j1
                return result.next
            if j1.val <= j2.val:
                jr.next = j1
                j1 = j1.next
            else:
                jr.next = j2
                j2 = j2.next
            jr = jr.next

# l1 = ListNode().arr2list([1,3,5])
# l2 = ListNode().arr2list([2,2,3])
# result = Solution().mergeTwoLists(l1, l2)
# print(result)