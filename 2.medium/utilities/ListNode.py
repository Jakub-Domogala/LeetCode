class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        jumper = self
        result = ''
        while jumper is not None:
            result += str(jumper.val) + " -> "
            jumper = jumper.next
        return result
    
    def arr2list(self, arr):
        result = None
        for v in arr[::-1]:
            result = ListNode(v, result)
        return result

    def list2arr(self):
        jumper = self
        arr = []
        while jumper is not None:
            arr.append(jumper.val)
            jumper = jumper.next
        return arr

    def appendleft(self, element):
        return ListNode(element, self)

    def append(self, element):
        jumper = self
        while jumper.next is not None:
            jumper = jumper.next
        jumper.next = ListNode(element)
        return self
    
    def remove_nth(self, n):
        if self.size() <= n or n < 0:
            return False
        if n == 0:
            return self.next
        jumper = self
        for _ in range(n-1):
            jumper = jumper.next
        jumper.next = jumper.next.next
        return self

    def remove_nth_from_end(self, n):
        return self.remove_nth(self.size() - n - 1)

    def size(self):
        jumper, result = self, 1
        while jumper.next is not None:
            jumper = jumper.next
            result += 1
        return result


# arr = [1, 2, 3]
# l1 = ListNode().arr2list(arr)
# l1 = l1.appendleft(4)
# l1 = l1.append(7)
# print(l1, l1.size())
# l1 = l1.remove_nth_from_end(0)
# print(l1)
# print(l1, l1.size())

# arr = l1.list2arr()
# print(arr)
