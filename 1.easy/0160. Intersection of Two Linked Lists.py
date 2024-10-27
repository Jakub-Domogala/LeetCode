# Time Complexity:   O(n)
# Memory Complexity: O(n)


from utilities.ListNode import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        jmp = headA
        setA = set()
        while jmp:
            setA.add(jmp)
            jmp = jmp.next
        jmp = headB
        while not jmp in setA and jmp:
            jmp = jmp.next
        if jmp in setA:
            return jmp
        return None
