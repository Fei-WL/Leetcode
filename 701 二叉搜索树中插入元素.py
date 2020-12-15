from Tree import TreeNode

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def deep(node: TreeNode, val: int):
            if val > node.val:
                if node.right:
                    deep(node.right, val)
                else:
                    node.right = TreeNode(val)
                    return
            if val < node.val:
                if node.left:
                    deep(node.left, val)
                else:
                    node.left = TreeNode(val)
                    return

        if root is None:
            return TreeNode(val)

        deep(root, val)

        return root