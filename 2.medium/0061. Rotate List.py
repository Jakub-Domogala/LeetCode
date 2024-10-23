# Time Complexity:   O(n)
# Memory Complexity: O(1)


from utilities.ListNode import ListNode
from typing import Optional

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head:
            return head
        def get_n(head):
            cnt = 0
            jmp = head
            while jmp:
                cnt += 1
                jmp = jmp.next
            return cnt
        n = get_n(head)
        k %= n
        if k == 0:
            return head
        new_end = head
        for i in range(n-k-1):
            new_end = new_end.next
        new_head = new_end.next
        new_end.next = None
        jmp = new_head
        for i in range(k-1):
            jmp = jmp.next
        jmp.next = head
        return new_head


# arr = [1,2,3,4]
# k = 5
# lst = ListNode().arr2list(arr)
# print(lst)
# result = Solution().rotateRight(lst, k)
# print(result)
