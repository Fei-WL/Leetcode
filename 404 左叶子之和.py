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
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.result = 0
        def deep(node: TreeNode):
            if node.left:
                if node.left.left is None and node.left.right is None:
                    self.result += node.left.val
                deep(node.left)
            if node.right:
                deep(node.right)

        deep(root)
        return self.result

input = "[1,2,3,4,5]"
root = stringToTreeNode(input)
s = Solution()
print(s.sumOfLeftLeaves(root))