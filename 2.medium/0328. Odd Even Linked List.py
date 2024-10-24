# Time Complexity:   O(n)
# Memory Complexity: O(1)
#
# Also beats 100% in runtime and 97% in memory


from typing import Optional
from utilities.ListNode import ListNode

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        h0, h1 = None, None
        jmp0, jmp1 = None, None
        jmp = head
        cnt = 0
        while jmp:
            if cnt % 2 == 0:
                if not h0:
                    h0 = jmp0 = jmp
                else:
                    jmp0.next = jmp
                    jmp0 = jmp
            else:
                if not h1:
                    h1 = jmp1 = jmp
                else:
                    jmp1.next = jmp
                    jmp1 = jmp
            jmp = jmp.next
            cnt += 1
        if jmp0:
            jmp0.next = h1
        if jmp1:
            jmp1.next = None
        return h0


# arr = [1,2,3,4,5]
# lst = ListNode().arr2list(arr)
# print("In ", lst)
# lst = Solution().oddEvenList(lst)
# print("Out",lst)
