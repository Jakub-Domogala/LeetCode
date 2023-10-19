from typing import Optional

from utilities.ListNode import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        back = head
        front = head.next
        while front and front.next:
            front = front.next.next
            back = back.next
            if back == front:
                return True
        return False
