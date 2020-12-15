from ListNode import ListNode, stringToListNode

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head

        point = head
        headlist = []
        while point:
            headlist.append(point)
            point = point.next

        prev = ListNode(0)
        for index in range(0, len(headlist), 2):
            headlist[index].next = headlist[index + 1].next
            headlist[index + 1].next = headlist[index]
            prev.next = headlist[index + 1]
            prev = headlist[index]

        return headlist[1]

input = "[1,2,3,4]"
head = stringToListNode(input)
Solution().swapPairs(head)