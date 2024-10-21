from utilities.ListNode import ListNode
from typing import Optional


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def get_len(head):
            cnt, jmp = 0, head
            while jmp:
                jmp = jmp.next
                cnt += 1
            return cnt
        n = get_len(head)
        jmp = head
        buffor = []
        for i in range(n//2):
            buffor.append(jmp.val)
            jmp = jmp.next
        if n%2 == 1:
            jmp = jmp.next
        for i in range(n//2):
            v = buffor.pop()
            if v != jmp.val:
                return False
            jmp = jmp.next
        return True


# arr = [1,2,2,1]
# lst = ListNode().arr2list(arr)
# print(lst)
# result = Solution().isPalindrome(lst)
# print(result, True)
# arr = [1,2,1]
# lst = ListNode().arr2list(arr)
# print(lst)
# result = Solution().isPalindrome(lst)
# print(result, True)
# arr = [1,2,2]
# lst = ListNode().arr2list(arr)
# print(lst)
# result = Solution().isPalindrome(lst)
# print(result, False)
# arr = [1,2,2,2]
# lst = ListNode().arr2list(arr)
# print(lst)
# result = Solution().isPalindrome(lst)
# print(result, False)
