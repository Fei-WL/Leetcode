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
    def inorderTraversal(self, root: TreeNode):
        self.result = []

        def mid_deep(node:TreeNode):
            if node.left:
                mid_deep(node.left)
            self.result.append(node.val)
            if node.right:
                mid_deep(node.right)

        if root:
            mid_deep(root)
        else:
            return self.result

        return self.result

s = Solution()
input = "[1,null,2,3]"
root = stringToTreeNode(input)
print(s.inorderTraversal(root))