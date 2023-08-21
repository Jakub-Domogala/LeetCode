# Time Complexity:   O(n)
# Memory Complexity: O(n)

from utilities.ListNode import ListNode

class Solution(object):
    def swapPairs(self, head: ListNode) -> ListNode:
        return head.swap_pairs()

l1 = Solution().swapPairs(ListNode().arr2list([1, 2, 3, 4, 5, 6, 7, 8]))
print(l1)
                
            

