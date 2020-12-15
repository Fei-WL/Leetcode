from Tree import TreeNode
from typing import List

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None

        root = TreeNode(postorder[-1])
        in_res = inorder.index(postorder[-1])
        left_inorder = inorder[:in_res]
        right_inorder = inorder[in_res+1:]
        left_len = len(left_inorder)
        right_len = len(right_inorder)
        left_postorder = postorder[:left_len]
        right_postorder = postorder[-(1+right_len):-1]
        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)
        return root

inorder = [1,2,3,4]
postorder = [1,4,3,2]

root = Solution().buildTree(inorder, postorder)
print(root)