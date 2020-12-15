from Tree import TreeNode, stringToTreeNode

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.minminus = 99999
        minuslist = []

        def middle(node: TreeNode):
            if node.left:
                # minuslist.append(node.left.val)
                middle(node.left)

            minuslist.append(node.val)

            if len(minuslist) >= 2:
                temp = abs(minuslist[-1] - minuslist[-2])
                if self.minminus > temp:
                    self.minminus = temp

            if node.right:
                # minuslist.append(node.right.val)
                middle(node.right)

        middle(root)
        return self.minminus

input = "[1,null,3,2]"
root = stringToTreeNode(input)
Solution().getMinimumDifference(root)