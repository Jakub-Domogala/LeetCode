# Time Complexity:   O(n)
# Memory Complexity: O(1)


from typing import Optional
from utilities.ListNode import ListNode

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def get_n(node):
            jmp = node
            cnt = 0
            while jmp:
                jmp = jmp.next
                cnt += 1
            return cnt
        def create_ord_n_rev_parts(head, n):
            h_ord = head
            h_rev = None
            t_rev = None
            jmp = head
            for i in range((n+1)//2-1):
                jmp = jmp.next
            tmp = jmp.next
            jmp.next = None
            jmp = tmp
            for i in range((n)//2):
                tmp = jmp.next
                jmp.next = h_rev
                h_rev = jmp
                jmp = tmp
            return h_ord, h_rev
        def merge_parts(h_ord, h_rev, n):
            back_ord, front_ord = None, h_ord
            back_rev, front_rev = None, h_rev
            for i in range(n):
                if i%2 == 1:
                    back_ord.next = back_rev
                    back_rev.next = front_ord
                else:
                    back_rev = front_rev
                    if front_rev:
                        front_rev = front_rev.next
                    back_ord = front_ord
                    front_ord = front_ord.next

        n = get_n(head)
        h_ord, h_rev = create_ord_n_rev_parts(head, n)
        merge_parts(h_ord, h_rev, n)


# arr = [1,2,3,4,5]
# lst = ListNode().arr2list(arr)
# print("In ", lst)
# Solution().reorderList(lst)
# print("Out",lst)
