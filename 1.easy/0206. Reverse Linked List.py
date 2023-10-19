# Time Complexity:   O(n)
# Memory Complexity: O(1)

from typing import Optional

from utilities.ListNode import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        jumper = head
        while jumper:
            prev = jumper
            jumper = jumper.next
            prev.next = new_head
            new_head = prev
        return new_head
