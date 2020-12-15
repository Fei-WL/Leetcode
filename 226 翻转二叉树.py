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

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.result = []

        def after_deep(node: TreeNode):
            if node.left:
                after_deep(node.left)
            if node.right:
                after_deep(node.right)
            temp = node.left
            node.left = node.right
            node.right = temp

        if root:
            after_deep(root)
        else:
            return root

        return root

input = "[4,2,7,1,3,6,9]"
root = stringToTreeNode(input)
s = Solution()
print(s.invertTree(root))