class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        self.balance = True

        def searchDFS(root, val):
            if root is None:
                return val

            depLeft = searchDFS(root.left, val + 1)
            depRight = searchDFS(root.right, val + 1)

            if abs(depLeft - depRight) > 1:
                self.balance = False

            return max(depLeft, depRight)

        searchDFS(root, 0)

        return self.balance