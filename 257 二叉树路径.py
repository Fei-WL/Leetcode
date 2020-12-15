class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode):
        self.result = []
        temp = []
        self.deep_find(root, temp)
        return self.result

    def deep_find(self, node: TreeNode, path_list: list):
        if node:
            path_list.append(str(node.val))
            if node.left or node.right:
                self.deep_find(node.left, path_list)
                self.deep_find(node.right, path_list)
            else:
                self.result.append('->'.join(path_list))
                path_list.pop()
                return

            if len(path_list) > 1:
                path_list.pop()
                return

        else:
            return
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
input = "[1,2,3,null,5]"
root=stringToTreeNode(input)
print(s.binaryTreePaths(root))