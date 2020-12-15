from Tree import stringToTreeNode
from Tree import TreeNode as Node

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        parents = []
        parents.append(root)
        while len(parents) != 0:
            limit = len(parents)
            while limit != 0:
                if limit > 1:
                    parents[0].next = parents[1]
                limit -= 1
                if parents[0].left:
                    parents.append(parents[0].left)
                if parents[0].right:
                    parents.append(parents[0].right)
                parents.pop(0)
        return root

input = "[1,2,3,4,null,6,7]"
root = stringToTreeNode(input)
print(Solution().connect(root))