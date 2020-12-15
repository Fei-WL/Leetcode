"""
二叉搜索树是一棵空树，或者是具有下列性质的二叉树：

若它的左子树不空，则左子树上所有节点的值均小于它的根节点的值；

若它的右子树不空，则右子树上所有节点的值均大于它的根节点的值；

它的左、右子树也分别为二叉搜索树。

由这样的性质我们可以发现，二叉搜索树的中序遍历是一个单调递增的有序序列。如果我们反序地中序遍历该二叉搜索树，即可得到一个单调递减的有序序列。
"""
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
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        def deep(node, node_list):
            if node.left:
                deep(node.left, node_list)
            node_list.append(node)
            if node.right:
                deep(node.right, node_list)

        node_list = []
        deep(root, node_list)
        node_list = sorted(node_list, key=lambda k:(k.val))
        val_list = [node.val for node in node_list]
        val_list.reverse()
        for index in range(len(node_list)):
            stop = val_list.index(node_list[index].val)
            if stop != -1:
                node_list[index].val += sum(val_list[:stop])

        return root


s = Solution()
input = "[5,2,13]"
root = stringToTreeNode(input)
print(s.convertBST(root))