# Time Complexity:   O(max(n1, n2))
# Memory Complexity: O(1)
# Where n1 and n2 are lengths of l1 and l2

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def arr2list(self, arr):
        if len(arr) == 0:
            return None
        result = ListNode(arr[0])
        jumper = result
        for i in range(1, len(arr)):
            jumper.next = ListNode(arr[i])
            jumper = jumper.next
        return result

    def print(self):
        jumper = self
        while jumper is not None:
            print(jumper.val, "->", end=" ")
            jumper = jumper.next
        print(None)


class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(None)
        result_arr = []
        r_jumper = result
        j1 = l1
        j2 = l2
        rest = 0
        while True:
            tmp = rest + j1.val + j2.val
            rest = tmp // 10
            n_val = tmp % 10
            r_jumper.next = ListNode(n_val)
            r_jumper = r_jumper.next
            result_arr.append(r_jumper.val)
            if rest == 0 and j1.next is None and j2.next is None:
                print(result_arr)
                return result.next
            j1 = j1.next if j1.next is not None else ListNode(0)
            j2 = j2.next if j2.next is not None else ListNode(0)


# arr1 = [2, 4, 3]
# arr2 = [5, 6, 4]
# l1 = ListNode().arr2list(arr1)
# l2 = ListNode().arr2list(arr2)
# print(Solution().addTwoNumbers(l1, l2))
