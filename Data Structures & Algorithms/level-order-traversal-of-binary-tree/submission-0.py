class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.fin = []  # stores each level of the tree

        def binDepSearch(root, dep):
            if root is None:  # stop if there is no node
                return

            if dep == len(self.fin):  # if this level does not exist yet
                self.fin.append([])  # create a new list for this level

            self.fin[dep].append(root.val)  # add the node's value to its depth

            binDepSearch(root.left, dep + 1)  # search the left subtree
            binDepSearch(root.right, dep + 1)  # search the right subtree

        binDepSearch(root, 0)  # start at depth 0

        return self.fin