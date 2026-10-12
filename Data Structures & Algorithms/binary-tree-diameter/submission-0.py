# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest = 0
        def searchDFS(root):
            if root is None:
                return 0
            leftDep = searchDFS(root.left)
            rightDep = searchDFS(root.right)
            self.longest = max(self.longest, leftDep + rightDep)
            return 1 + max(leftDep, rightDep)

        searchDFS(root)
        return self.longest
        