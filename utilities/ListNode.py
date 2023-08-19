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

    def list2arr(self):
        jumper = self
        arr = []
        while jumper is not None:
            arr.append(jumper.val)
            jumper = jumper.next
        return arr

    def __str__(self):
        jumper = self
        result = ''
        while jumper is not None:
            result += str(jumper.val) + " -> "
            jumper = jumper.next
        result += '\n'
        return result

    def appendleft(self, element):
        return ListNode(element, self)

    def append(self, element):
        jumper = self
        while jumper.next is not None:
            jumper = jumper.next
        jumper.next = ListNode(element)
        return self


# arr = [1, 2, 3]
# l1 = ListNode().arr2list(arr)
# l1 = l1.appendleft(4)
# l1 = l1.append(7)
# print(l1)
# arr = l1.list2arr()
# print(arr)
