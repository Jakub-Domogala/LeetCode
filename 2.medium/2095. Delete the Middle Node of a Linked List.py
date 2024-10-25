# Time Complexity:   O(n)
# Memory Complexity: O(1)


from typing import Optional, List
from utilities.ListNode import ListNode


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_n(head):
            jmp = head
            cnt = 0
            while jmp:
                cnt += 1
                jmp = jmp.next
            return cnt
        n = get_n(head)
        if n == 1:
            return None
        i = n//2
        jmp = head
        for i in range(i-1):
            jmp = jmp.next
        after = jmp.next.next
        jmp.next = after
        return head

arr = [1,2,3,4,5,6,7]
lst = ListNode().arr2list(arr)
result = Solution().deleteMiddle(lst)
print(result)
