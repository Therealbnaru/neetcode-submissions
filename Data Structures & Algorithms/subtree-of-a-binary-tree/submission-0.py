class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        if root.val == subRoot.val:
            if self.matches(root, subRoot) == True:
                return True

        if self.isSubtree(root.left, subRoot) == True:
            return True

        if self.isSubtree(root.right, subRoot) == True:
            return True

        return False

    def matches(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True

        elif root is None or subRoot is None:
            return False

        elif root.val != subRoot.val:
            return False

        if self.matches(root.left, subRoot.left) == False:
            return False

        if self.matches(root.right, subRoot.right) == False:
            return False

        return True