from ListNode import ListNode

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None
        current = head
        next_node = head.next
        while next_node:
            if next_node.val == val:
                current.next = next_node.next
                next_node.next = None
                return head
            else:
                current = current.next
                next_node = next_node.next
        if head.val == val:
            return head.next