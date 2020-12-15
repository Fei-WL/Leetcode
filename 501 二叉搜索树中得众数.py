from Tree import stringToTreeNode, TreeNode
from typing import List

class Solution():
    def findMode(self, root: TreeNode) -> List[int]:
        self.dic = {}

        def deep(node: TreeNode):
            if node.val not in self.dic.keys():
                self.dic[node.val] = 1
            else:
                self.dic[node.val] += 1
            if node.left:
                deep(node.left)
            if node.right:
                deep(node.right)

        if root is None:
            return []

        deep(root)
        self.dic = dict(sorted(self.dic.items(), key=lambda kv:(kv[1], kv[0]), reverse=True))

        flag = 0
        for index in range(len(list(self.dic.values()))):
            if list(self.dic.values())[index] < list(self.dic.values())[0]:
                flag = index

        if flag == 0:
            return list(self.dic.keys())[flag]
        else:
            return list(self.dic.keys())[:flag]

input = "[2147483647]"
root = stringToTreeNode(input)
print(Solution().findMode(root))