# Definition for singly-linked list.
from ListNode import ListNode, stringToIntegerList, stringToListNode, listNodeToString

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node = head
        temp_list = []
        while node:
            temp_list.append(node)
            node = node.next
        if len(temp_list) < n + 1:
            return head.next
        if n == 1:
            temp_list[-2].next = None
            return head
        prior = temp_list[-(n+1)]
        next = temp_list[-(n-1)]
        prior.next = next
        return head


line = "[1,2]"
head = stringToListNode(line)
n = 1
print(listNodeToString(Solution().removeNthFromEnd(head, n)))