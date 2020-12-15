class TreeNode(object):
    def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []

        order_list = [root]
        while len(order_list) != 0:
            count = len(order_list)
            temp = []
            for _ in range(count):
                node = order_list.pop(0)
                temp.append(node.val)
                if node.left:
                    order_list.append(node.left)
                if node.right:
                    order_list.append(node.right)
            result.append(temp)
        return result[::-1]


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root
s = Solution()
input = "[3,9,20,null,null,15,7]"
root = stringToTreeNode(input)
print(s.levelOrderBottom(root))