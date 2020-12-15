# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        while fast != None:
            slow = slow.next
            if fast.next == None:
                return None
            fast = fast.next.next

            if slow == fast:
                start = head
                while start != slow:
                    start = start.next
                    slow = slow.next
                return start

        return None