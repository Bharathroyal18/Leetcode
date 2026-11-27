# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:


        result = []

        def preorder(node):
            if node is None:
                return

            result.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return result


        # stack = []
        # result = []       this is stack and iterative approach

        # if root:
        #     stack.append(root)

        # while stack:
        #     node = stack.pop()
        #     result.append(node.val)

        #     if node.right:
        #         stack.append(node.right)

        #     if node.left:
        #         stack.append(node.left)

        # return result