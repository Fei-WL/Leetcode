from Tree import TreeNode, stringToTreeNode

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val > root.val\
                or p.val > root.val and q.val < root.val:
            return root
        elif p.val == root.val:
            return root
        elif q.val == root.val:
            return root
        else:
            if root.left:
                result = self.lowestCommonAncestor(root.left, p, q)
                if result:
                    return result
            if root.right:
                result = self.lowestCommonAncestor(root.right, p, q)
                if result:
                    return result

input = "[6,2,8,0,4,7,9,null,null,3,5]"
root = stringToTreeNode(input)
p = TreeNode(5)
q = TreeNode(0)
print(Solution().lowestCommonAncestor(root, p, q).val)