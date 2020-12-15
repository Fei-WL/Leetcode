from typing import List
from Tree import TreeNode, stringToTreeNode

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.result = []
        if root is None:
            return self.result

        def deep(node, path, total, num):
            path = path[:]
            path += [node.val]
            total += node.val
            if node.left is None and node.right is None:
                if total == num:
                    self.result.append(path)
            else:
                if node.left:
                    deep(node.left, path, total, num)
                if node.right:
                    deep(node.right, path, total, num)
            return

        path = []
        total = 0
        deep(root, path, total, sum)

        return self.result

input = "[5,4,8,11,null,13,4,7,2,null,null,5,1]"
sum = 22
root = stringToTreeNode(input)
print(Solution().pathSum(root, sum))