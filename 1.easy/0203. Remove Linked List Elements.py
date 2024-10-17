# Time Complexity:   O(n)
# Memory Complexity: O(1)


from os import remove
from utilities.ListNode import ListNode
from typing import Optional

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        before = ListNode(None, head)
        new_head = before
        after = head
        while after:
            if after.val != val:
                before = after
                after = after.next
            else:
                after = after.next
                before.next = after
        return new_head.next

arr = [5,0,1,2,5,3,2,5]
val = 5
lst = ListNode().arr2list(arr)
print(lst)
result = Solution().removeElements(lst, val)
print(result)
