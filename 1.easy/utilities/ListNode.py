from typing import Any, Type, List

class ListNode(object):
    def __init__(self, val: Any = 0, next: Type["ListNode"] = None) -> Type["ListNode"]:
        self.val: Any = val
        self.next: Type["ListNode"] = next
    
    def __str__(self) -> str:
        jumper = self
        result = ''
        while jumper is not None:
            result += str(jumper.val) + " -> "
            jumper = jumper.next
        return result
    
    def arr2list(self, arr: List) -> Type["ListNode"]:
        result = None
        for v in arr[::-1]:
            result = ListNode(v, result)
        return result

    def list2arr(self) -> List:
        jumper = self
        arr = []
        while jumper is not None:
            arr.append(jumper.val)
            jumper = jumper.next
        return arr

    def appendleft(self, element: Type["ListNode"]) -> Type["ListNode"]:
        return ListNode(element, self)

    def append(self, element: Type["ListNode"]) -> Type["ListNode"]:
        jumper = self
        while jumper.next is not None:
            jumper = jumper.next
        jumper.next = ListNode(element)
        return self
    
    def remove_nth(self, n: int) -> Type["ListNode"]:
        if self.size() <= n or n < 0:
            return False
        if n == 0:
            return self.next
        jumper = self
        for _ in range(n-1):
            jumper = jumper.next
        jumper.next = jumper.next.next
        return self

    def remove_nth_from_end(self, n: int) -> Type["ListNode"]:
        return self.remove_nth(self.size() - n - 1)

    def size(self) -> int:
        jumper, result = self, 1
        while jumper.next is not None:
            jumper = jumper.next
            result += 1
        return result
    
    def swap_pairs(self) -> Type["ListNode"]:
        if not self.next:
            return self
        back = ListNode(None, self)
        result, front= self.next, self.next
        while front:
            # reattach pointers
            back.next.next, front.next, back.next = front.next, back.next, front
            # reposition front and back
            back, front = front.next, front.next.next
            if front is None:
                break
            front = front.next
        return result


# for i in range(1, 7):
#     l = ListNode().arr2list([x for x in range(i)])
#     l = l.swap_pairs()
#     print(l)
