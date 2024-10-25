# Time Complexity:   O(n)
# Memory Complexity: O(1)
#
# For each group of non 0 nums I add all .val's to the first one and delete the following numbers
# 2 moving pointers to not lose ending of the list


from typing import Optional, List
from utilities.ListNode import ListNode

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        b_jmp = b_head = ListNode(0, head)
        jmp = head
        while jmp:
            if jmp.val == 0:
                b_jmp.next = jmp.next
                b_jmp = jmp
            elif b_jmp.val != 0:
                b_jmp.val += jmp.val
                b_jmp.next = jmp.next
            else:
                b_jmp = jmp
            jmp = jmp.next
        return b_head.next

# arr = [7,3,1,0,4,5,2,0,1,1]
# lst = ListNode().arr2list(arr)
# print(lst)
# lst = Solution().mergeNodes(lst)
# print(lst)
