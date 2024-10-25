from collections import defaultdict
from typing import Optional, List
from typing_extensions import DefaultDict
from utilities.ListNode import ListNode

class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        is_in_nums = defaultdict(bool)
        for e in nums:
            is_in_nums[e] = True
        last = False
        jmp = head
        cnt = 0
        while jmp:
            if is_in_nums[jmp.val]:
                if not last:
                    cnt += 1
                    last = True
            else:
                last = False
            jmp = jmp.next
        return cnt


arr = [0,1,2,3]
nums = [0,1,3]
lst = ListNode().arr2list(arr)
result = Solution().numComponents(lst, nums)
print(result)
