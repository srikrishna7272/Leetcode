# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # res = []
        # if not root:
        #     return res
        # def preorder(root):
        #     if root:
        #         res.append(root.val)
        #         preorder(root.left)
        #         preorder(root.right)
        # preorder(root)
        # return res

        res,stack = [], []
        curr = root

        while curr or stack:
            if curr:
                res.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()
        return res