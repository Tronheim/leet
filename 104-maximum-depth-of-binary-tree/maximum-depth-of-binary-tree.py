class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        L = self.maxDepth(root.left)
        R = self.maxDepth(root.right)

        return max(L,R) + 1