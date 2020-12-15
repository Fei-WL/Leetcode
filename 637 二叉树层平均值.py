class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

class Solution:
    def averageOfLevels(self, root: TreeNode):
        result = []
        tree_queue = [root]
        while len(tree_queue) != 0:
            sum_list = [node.val for node in tree_queue]
            result.append(sum(sum_list) / len(tree_queue))
            t_len = len(tree_queue)
            for index in range(t_len):
                if tree_queue[index].left:
                    tree_queue.append(tree_queue[index].left)
                if tree_queue[index].right:
                    tree_queue.append(tree_queue[index].right)
            tree_queue = tree_queue[t_len:]
        return result

s = Solution()
root = "[3,9,20,15,7]"
root = stringToTreeNode(root)
print(s.averageOfLevels(root))