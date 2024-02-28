from typing import Any, Type, List


class ListNode(object):
    def __init__(self, val: Any = 0, next: Type["ListNode"] = None) -> Type["ListNode"]:
        self.val: Any = val
        self.next: Type["ListNode"] = next

    def __str__(self) -> str:
        sep = " -> "
        if not self.is_cyclic():
            jumper = self
            result = ""
            while jumper is not None:
                result += str(jumper.val) + sep
                jumper = jumper.next
            return result
        return "cyclic TODO: printing"

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
            return None
        if n == 0:
            return self.next
        jumper = self
        for _ in range(n - 1):
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
        result, front = self.next, self.next
        while front:
            # reattach pointers
            back.next.next, front.next, back.next = front.next, back.next, front
            # reposition front and back
            back, front = front.next, front.next.next
            if front is None:
                break
            front = front.next
        return result

    def get_node(self, idx: int) -> Type["ListNode"]:
        result, i = self, 0
        while result:
            if i == idx:
                return result
            result = result.next
            i += 1
        return None

    def is_cyclic(self) -> bool:
        back = self
        front = self.next
        while front and front.next:
            front = front.next.next
            back = back.next
            if back == front:
                return True
        return False

    def make_cycle(self, dest_idx: int) -> Type["ListNode"]:
        if dest_idx >= self.size():
            return False
        end = self.get_node(self.size() - 1)
        dest = self.get_node(dest_idx)
        end.next = dest
        return self

    def size_cyclic(self) -> int:
        if not self.is_cyclic():
            return None
        back = self
        front = self.next
        while back != front:
            back, front = back.next, front.next.next
        i = 1
        while back != front.next:
            front = front.next
            i += 1
        return i

    def remove_duplicates_from_sorted(self) -> Type["ListNode"]:
        if self is None or self.next is None:
            return self
        back = self
        front = self
        while front.next:
            front = front.next
            if back.val == front.val:
                back.next = front.next
            else:
                back = front
        return self


# l = ListNode().arr2list([x for x in range(5)])
# print(l)
# l.make_cycle(2)
# print(l.size_cyclic())
# # l = l.swap_pairs()
# print(l)

# arr = [1,1,2,2,3,4,5,5]
# lst = ListNode().arr2list(arr)
# print(lst)
# lst.remove_duplicates_from_sorted()
# print(lst)
