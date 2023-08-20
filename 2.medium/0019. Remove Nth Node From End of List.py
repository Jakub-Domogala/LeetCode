from utilities.ListNode import ListNode

class Solution(object):
    def removeNthFromEnd(self, head: ListNode, n):
        return head.remove_nth_from_end(n)

# arr = [1, 2, 3, 4, 5, 6]
# l1 = ListNode().arr2list(arr)
# print(l1, l1.size())
# l1 = l1.remove_nth_from_end(1)
# print(l1, l1.size())
