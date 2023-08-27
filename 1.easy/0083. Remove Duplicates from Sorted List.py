# Time Complexity:   O(n)
# Memory Complexity: O(1)

from utilities.ListNode import ListNode


class Solution(object):
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
        back = head
        front = head
        while front.next:
            front = front.next
            if back.val == front.val:
                back.next = front.next
            else:
                back = front
        return head

# arr = [1,1,2,2,3,4,5,5]
# lst = ListNode().arr2list(arr)
# print(lst)
# # lst = Solution().deleteDuplicates(lst)
# Solution().deleteDuplicates(lst)
# print(lst)


    
                    
            
            