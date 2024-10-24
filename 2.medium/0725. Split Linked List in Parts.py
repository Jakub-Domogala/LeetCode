# Time Complexity:   O(n)
# Memory Complexity: O(n)


from utilities.ListNode import ListNode
from typing import Optional, List

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if k <= 0:
            raise ValueError("k value has to be positive integer")
        def get_n(head):
            cnt = 0
            jmp = head
            while jmp:
                cnt += 1
                jmp = jmp.next
            return cnt
        n = get_n(head)
        part_size, overhead = n//k, n%k
        result = []
        jmp = head
        for i in range(k):
            result.append(jmp)
            curr_size = part_size + (1 if overhead > 0 else 0)
            overhead = max(0, overhead-1)
            for j in range(curr_size - 1):
                jmp = jmp.next
            if jmp:
                new_start = jmp.next
                jmp.next = None
                jmp = new_start
        return result



# arr = [1,2,3,4,5,6,7,8]
# k = 5
# lst = ListNode().arr2list(arr)
# print(lst)
# result = Solution().splitListToParts(lst, k)
# for r in result:
#     print(r)
# print("="*20)
# arr = [1,2,3]
# k = 5
# lst = ListNode().arr2list(arr)
# print(lst)
# result = Solution().splitListToParts(lst, k)
# for r in result:
#     print(r)
